import os
from time import sleep
from datetime import datetime
import csv
import platform

# start instructions with a delay (in seconds)
waitforinstr = 7

# start points of bio-calibration parts (in seconds)
marker_eyesclosed = 25
marker_jawclench = 45
marker_leftright = 65

# duration of recording
duration = 300

# get starting timestamp
start = datetime.now()
update = datetime.now()

# initialize stuff for markers
marker = ""
soundinstr_init = True
sound0_init = True
sound1_init = True
sound2_init = True
sound3_init = True
sound4_init = True
sound5_init = True
sound6_init = True

# store markers and send tones
with open(
    "markers_sleep_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv", "w"
) as f:
    while update.timestamp() < start.timestamp() + duration:

        # play instructions
        if soundinstr_init and update.timestamp() > start.timestamp() + waitforinstr:
            print("\nwelcome!")
            print("relax and try not to move during the calibration phase")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'welcome  '")
                os.system("say ' '")
                os.system(
                    "say 'relax and try not to move during the calibration phase'"
                )
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('welcome  ')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' ')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('relax and try not to move during the calibration phase')\""
                )
            soundinstr_init = False

        # create marker and give instructions
        if sound0_init and update.timestamp() > start.timestamp() + marker_eyesclosed:
            print("\nclose your eyes for ten seconds")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'close your eyes for ten seconds'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('close your eyes for ten seconds')\""
                )
            marker = "eyes_closed_10s"
            sound0_init = False

        # give instructions
        if (
            sound1_init
            and update.timestamp() > start.timestamp() + marker_eyesclosed + 17
        ):
            print("\nopen your eyes")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'open your eyes'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('open your eyes')\""
                )
            marker = ""
            sound1_init = False

        if sound2_init and update.timestamp() > start.timestamp() + marker_jawclench:
            print("\nclench your teeth every second for ten seconds")
            print("start now")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'clench your teeth every second for ten seconds'")
                os.system("say 'start now'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('clench your teeth every second for ten seconds')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('start now')\""
                )
            marker = "jawclench_10s"
            sound2_init = False

        if (
            sound3_init
            and update.timestamp() > start.timestamp() + marker_jawclench + 17
        ):
            print("\nrelax")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'relax'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('relax')\""
                )
            marker = ""
            sound3_init = False

        if sound4_init and update.timestamp() > start.timestamp() + marker_leftright:
            print("\nwith your eyes only, look to the left and to the right")
            print("switch every second")
            print("start now")
            if platform.system() == "Darwin":  # mac os
                os.system(
                    "say 'with your eyes only, look to the left and to the right'"
                )
                os.system("say 'switch every second'")
                os.system("say 'start now'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('with your eyes only, look to the left and to the right')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('switch every second')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('start now')\""
                )
            marker = "leftright_10s"
            sound4_init = False

        if (
            sound5_init
            and update.timestamp() > start.timestamp() + marker_leftright + 17
        ):
            print("\nrelax")
            if platform.system() == "Darwin":  # mac os
                os.system("say 'relax'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('relax')\""
                )
            marker = ""
            sound5_init = False

        if (
            sound6_init
            and update.timestamp() > start.timestamp() + marker_leftright + 25
        ):
            print("\nnow you can go to bed")
            print(
                "\n**********************\nHAVE A WONDERFUL NIGHT\n**********************"
            )
            if platform.system() == "Darwin":  # mac os
                os.system("say 'now you can go to bed'")
                os.system("say 'have a wonderful night'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('now you can go to bed')\""
                )
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('have a wonderful night')\""
                )
            sound6_init = False

        # write to csv file
        update = datetime.now()
        writer = csv.writer(f)
        writer.writerow([update.timestamp() + 3600, marker])

        # this ensures that the marker file is not too large
        sleep(0.1)
