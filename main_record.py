import asyncio
from idun_guardian_client import GuardianClient
import csv
from datetime import datetime
import subprocess
import os

# clear workspace
os.system("cls" if os.name == "nt" else "clear")
print(
    "\n\n#########################################\n### WELCOME TO THE IDUN TEST PLATFORM ###\n#########################################\n\n"
)


# # # # # # # # # SEARCH # # # # # # # # # # # # #

# get device address
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())


# # # # # # # # # BATTERY # # # # # # # # # # # # #

# input check battery level
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_battery = input(
    "Check battery level?         \ny=yes, n=no                                   "
)

# display battery level
if check_battery == "y":

    # check battery
    asyncio.run(bci.start_battery())


# # # # # # # # # IMPEDANCE # # # # # # # # # # # # #

# input check impedance
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_impedance = input("Press ENTER to display impedance\n")

IMPEDANCE_DURATION = 5  # duration of impedance measurement in seconds
MAINS_FREQUENCY_60Hz = False
# mains frequency in Hz (50 or 60), for Europe 50Hz, for US 60Hz

# start a recording session
asyncio.run(
    bci.start_recording(
        recording_timer=IMPEDANCE_DURATION,
        mains_freq_60hz=MAINS_FREQUENCY_60Hz,
        impedance_measurement=True,
    )
)


# # # # # # # # # RECORDING # # # # # # # # # # # # #

# input select recording type
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
recording_type = input(
    "Select the type of recording \n1=open-end recording \n2=timed recording \n3=sleep recording \n4=eyes open - eyes closed experiment \n"
)

# open-end recording
if recording_type == "1":

    # define variables
    EXPERIMENT: str = "Open-End Recording"  # name of the experiment
    RECORDING_TIMER: int = 172800  # recording timer in seconds
    LED_SLEEP: bool = False  # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open(
        "info_openrec_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nOverall Comfort of the Device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            age = input("\nOptional: How old are you:                    ")
            gender = input("\nOptional: What is your gender:                ")
            print("\n\n--------------------------------")
            input("\nPress ENTER if you are ready to start the recording ")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            writer.writerow(["Age", age])
            writer.writerow(["Gender", gender])
            filling = False

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )


# timed recording
elif recording_type == "2":

    # define variables
    EXPERIMENT: str = "Timed Recording"  # name of the experiment
    RECORDING_TIMER = int(input("\nRecording Time (Seconds):                     "))
    LED_SLEEP: bool = False  # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open(
        "info_timedrec_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nOverall Comfort of the Device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            age = input("\nOptional: How old are you:                    ")
            gender = input("\nOptional: What is your gender:                ")
            print("\n\n--------------------------------")
            input("\nPress ENTER if you are ready to start the recording ")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            writer.writerow(["Age", age])
            writer.writerow(["Gender", gender])
            filling = False

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )


# sleep recording
elif recording_type == "3":

    # define variables
    EXPERIMENT: str = "Sleep"  # name of the experiment
    RECORDING_TIMER: int = 36000  # recording timer in seconds
    LED_SLEEP: bool = True  # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open(
        "info_sleep_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nOverall Comfort of the Device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            age = input("\nOptional: How old are you:                    ")
            gender = input("\nOptional: What is your gender:                ")
            print("\n\n--------------------------------")
            print("\nMake sure your speakers are on")
            input("\nPress ENTER if you are ready to start the bio-calibration ")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            writer.writerow(["Age", age])
            writer.writerow(["Gender", gender])
            filling = False

    # start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "sleep_experiment_utils.py"], shell=False)

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )

    # terminate subprocess
    p.kill()


# eoec recording
elif recording_type == "4":

    # define variables
    EXPERIMENT: str = "EOEC"  # name of the experiment
    RECORDING_TIMER: int = 140  # recording timer in seconds
    LED_SLEEP: bool = False  # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open(
        "info_eoec_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nOverall Comfort of the Device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            age = input("\nOptional: How old are you:                    ")
            gender = input("\nOptional: What is your gender:                ")
            print("\n\n--------------------------------")
            print("\nMake sure your speakers are on")
            input("\nPress ENTER if you are ready to start the experiment ")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            writer.writerow(["Age", age])
            writer.writerow(["Gender", gender])
            filling = False

    # start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "eoec_experiment_utils.py"], shell=False)

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )

    # terminate subprocess
    p.kill()
