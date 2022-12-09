import os
from time import sleep
from datetime import datetime
import csv
import platform

# start instructions with a delay (in seconds)
waitforinstr = 10

# duration until experiment starts (eyes open) (in seconds)
marker1 = 20

# duration of eyes open and eyes closed conditiions (in seconds)
marker2 = 60

# duration of recording
duration = 145

# get starting timestamp
start = datetime.now()
update = datetime.now()

# initialize stuff for markers
marker = ""
soundinstr_init = True
sound0_init     = True
sound1_init     = True
sound2_init     = True

# store markers and send tones
with open("markers_eoec_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w") as f:
    while update.timestamp() < start.timestamp() + duration:

        # play instructions
        if soundinstr_init and update.timestamp() > start.timestamp() + waitforinstr:
            print("\nwelcome!")
            print("relax and try not to move during the experiment")
            if platform.system() == "Darwin": # mac os
                os.system("say 'welcome  '")
                os.system("say ' '")
                os.system("say 'relax and try not to move during the experiment'")
            elif platform.system() == "Windows": # windows
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('welcome  ')\"")
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' ')\"")
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('relax and try not to move during the experiment')\"")
            soundinstr_init = False
            
        # create marker and play tones and the right time
        if sound0_init and update.timestamp() > start.timestamp() + marker1:
            print("\neyes open")
            if platform.system() == "Darwin": # mac os
                os.system("say 'eyes open'")
            elif platform.system() == "Windows": # windows
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('eyes open')\"")  
            marker = "eyes_open_"+str(marker2)+"s"
            sound0_init = False

        if sound1_init and update.timestamp() > start.timestamp() + marker1 + marker2:
            print("\nclose your eyes")
            if platform.system() == "Darwin": # mac os
                os.system("say 'close your eyes'")
            elif platform.system() == "Windows": # windows
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('close your eyes')\"")  
            marker = "eyes_closed_"+str(marker2)+"s"
            sound1_init = False

        if sound2_init and update.timestamp() > start.timestamp() + marker1 + 2*marker2:
            print("\nwell done, the experiment is finished")
            if platform.system() == "Darwin": # mac os
                os.system("say 'well done, the experiment is finished'")
            elif platform.system() == "Windows": # windows
                os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('well done, the experiment is finished')\"")  
            marker = ""
            sound2_init = False

        # write to csv file
        update = datetime.now()
        writer = csv.writer(f)
        writer.writerow([update.timestamp()+3600, marker])

        # this ensures that the marker file is not too large
        sleep(0.1)
