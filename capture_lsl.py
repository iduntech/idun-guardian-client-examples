from pylsl import StreamInlet, resolve_stream
from lsl_utils import find_index
import threading
from queue import Queue
import numpy as np
import mne
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt6 import QtCore, QtWidgets
import sys
import asyncio
from pyqtgraph import ColorMap


# Queues for EEG data and spectrogram plotting
SFREQ = 250              # Sampling frequency in Hz

BUFFER_SIZE = 10 * SFREQ  # Buffer will now store 5 seconds of data
HISTORY_SECONDS = 10     # Number of seconds to display in the spectrogram
PSD_CALC_INTERVAL = 25   # Calculate PSD every 25 samples

# --------------------- MULTITAPER PARAMETERS ---------------------
SPECTOGRAM_FREQUENCY_BINS = np.arange(1., 36., 1.)  # frequencies from 1 to 35 Hz
NUMBER_OF_CYCLES = SPECTOGRAM_FREQUENCY_BINS / 2.  # different number of cycle per frequency
WINDOW_SIZE = 4  # window size was 1s (which makes problems)
FREQUENCY_RESOLUTION = 1  # frequency resolution is 1 Hz
TIME_BANDWIDTH = (WINDOW_SIZE * FREQUENCY_RESOLUTION) / 2  # time_halfbandwidth

eeg_queue = []
spectrogram_queue = []
eeg_buffer = []
# Initialize the spectrogram history array
# This will have 'HISTORY_SECONDS' columns, one for each second of data
# Assuming we have 35 frequency bins and want to keep 5 seconds of data
spectrogram_history = np.zeros((35, 10 * SFREQ))

def calculate_spectrogram(eeg_data):
    """
    Calculate the spectrogram of the EEG data.

    Args:
        eeg_data (list): List of EEG samples.

    Returns:
        np.array: Spectrogram of the EEG data.
    """
    # Calculate the spectrogram
    psds, freqs = mne.time_frequency.psd_array_multitaper(eeg_data, sfreq=SFREQ, fmin=1, fmax=40)
    return psds, freqs

def get_classifier_prediction():
    global eeg_buffer, spectrogram_queue, eeg_queue

    idx = 0
    while True:
        if len(eeg_queue) != 0:
            eeg_sample = eeg_queue.pop(0)
            eeg_buffer.append(eeg_sample)

            idx += 1
            if idx >= SFREQ:
                spectogram_data = calculate_multitaper_powerspectrum(
                    eeg_buffer[-SFREQ:],  # Last 1 second of data
                    SPECTOGRAM_FREQUENCY_BINS,
                    NUMBER_OF_CYCLES,
                    TIME_BANDWIDTH,
                    SFREQ,
                )
                if len(spectrogram_queue) >= 10 * SFREQ:
                    spectrogram_queue.pop(0)  # Remove oldest second
                spectrogram_queue.append(spectogram_data)
                idx = 0


def calculate_multitaper_powerspectrum(
    experiment_filtered_eeg_data,
    spectogram_frequency_bins,
    number_of_cycles,
    time_bandwidth,
    sample_rate,
):
    experiment_filtered_eeg_data = np.array(experiment_filtered_eeg_data)
    eeg_data_reshaped = experiment_filtered_eeg_data.reshape(
        1, 1, len(experiment_filtered_eeg_data)
    )
    power = mne.time_frequency.tfr_array_multitaper(
        eeg_data_reshaped,
        sample_rate,
        freqs=spectogram_frequency_bins,
        n_cycles=number_of_cycles,
        time_bandwidth=time_bandwidth,
        output="power",
    )
    # The 'power' array has shape (n_epochs, n_channels, n_freqs, n_times)
    # You can get the spectrogram for a specific epoch and channel with:
    # Existing code
    spectogram_data = power[0, 0, :, :]
    spectogram_data = spectogram_data.reshape(spectogram_data.shape[0], -1)  # Flatten time dimension
    return spectogram_data


def get_eeg_samples(eeg_inlet):
    """
    Get the EEG samples.
    """
    while True:
        eeg_sample, _ = eeg_inlet.pull_sample()
        eeg_queue.append(eeg_sample)

class SpectrogramPlotter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        
        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QtWidgets.QVBoxLayout(self.main_widget)

        self.spectrogram_widget = pg.PlotWidget()
        layout.addWidget(self.spectrogram_widget)
        self.spectrogram_image = pg.ImageItem()
        colormap = pg.colormap.get('viridis')  # You can choose 'hot', 'jet', etc.
    #    Apply the colormap to the spectrogram image
        self.spectrogram_image.setLookupTable(colormap.getLookupTable())


        self.spectrogram_widget.addItem(self.spectrogram_image)
        
        # Set up axes for the spectrogram
        self.spectrogram_widget.getPlotItem().setLabels(left='Frequency (Hz)', bottom='Time (s)')
        self.spectrogram_widget.getPlotItem().showGrid(True, True, 0.7)

        # Correct the timer setup
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(int(1000))  # Update interval in milliseconds for 1 second

    def update_plot(self):
        global spectrogram_history, eeg_buffer, spectrogram_queue, eeg_queue

        if len(spectrogram_queue) > 0:
            # Concatenate the spectrogram data for the plot
            spectrogram_data_for_plot = np.concatenate(spectrogram_queue, axis=1)

            if spectrogram_data_for_plot.shape[1] > 10 * SFREQ:
                spectrogram_data_for_plot = spectrogram_data_for_plot[:, -10*SFREQ:]
            # Update the plot
            self.spectrogram_image.setImage(spectrogram_data_for_plot.T, autoLevels=True)

            # Set aspect ratio and axis ranges
            self.spectrogram_widget.getPlotItem().getViewBox().setAspectLocked(lock=False)
            self.spectrogram_widget.getPlotItem().setXRange(0, 10 * SFREQ)  # Display 10 seconds
            self.spectrogram_widget.getPlotItem().setYRange(1, 35)  # Assuming frequency range is 1 to 35 Hz







def eeg_classifier():
    """
    Main function to start EEG classification and plotting.
    """
    app = QtWidgets.QApplication(sys.argv)

    streams_available = resolve_stream()
    Encrypted_eeg_stream = "EEG_data"
    eeg_index = find_index(streams_available, Encrypted_eeg_stream)
    eeg_inlet = StreamInlet(streams_available[eeg_index])

    main_win = SpectrogramPlotter()
    main_win.show()

    eeg_samples_thread = threading.Thread(target=get_eeg_samples, args=(eeg_inlet,))
    classifier_thread = threading.Thread(target=get_classifier_prediction)

    eeg_samples_thread.start()
    classifier_thread.start()

    sys.exit(app.exec())  # This starts the Qt event loop


if __name__ == "__main__":
    eeg_classifier()
