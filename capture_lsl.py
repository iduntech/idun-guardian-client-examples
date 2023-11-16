from pylsl import StreamInlet, resolve_stream
from lsl_utils import find_index
import threading
from queue import Queue
import datetime

classifier_prediction_queue = Queue()
eeg_queue = Queue()


def get_classifier_prediction():
    """
    This function is used to get the classifier prediction from the data and adds it to the classifier

    Args:
        classifier: classifier

    Returns:
        None
    """
    while True:
        eeg_sample = eeg_queue.get()
        print(eeg_sample)
        # Make classification here

def get_eeg_samples(eeg_inlet):
    """
    This function is used to get the eeg samples

    Args:
        eeg_inlet (StreamInlet): eeg_inlet

    Returns:
        None
    """
    while True:
        eeg_sample, _ = eeg_inlet.pull_sample()
        eeg_queue.put(eeg_sample)


def eeg_classifier():
    """Send encrypted data to the LSL stream

    Args:
        encrypted_data_queue (asyncio.Queue): Queue containing encrypted data

    Returns:
        None
    """
    while True:
        streams_available = resolve_stream()
        Encrypted_eeg_stream = "EEG_data"

        eeg_index = find_index(streams_available, Encrypted_eeg_stream)
    
        eeg_inlet = StreamInlet(streams_available[eeg_index])

        eeg_samples_thread = threading.Thread(target=get_eeg_samples, args=(eeg_inlet,))

        classifier_thread = threading.Thread(
            target=get_classifier_prediction, args=()
        )

        eeg_samples_thread.start()
        classifier_thread.start()

        eeg_samples_thread.join()
        classifier_thread.join()


if __name__ == "__main__":
    eeg_classifier()
