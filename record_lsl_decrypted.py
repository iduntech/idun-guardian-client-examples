"""
Sample script for using the Guardian Earbud Client
- Start recording data from the Guardian Earbuds
"""
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "pylsl"])
import asyncio
from idun_guardian_client.client import GuardianClient
from lsl_decrypted_utils import stream_decrypted_data

EXPERIMENT: str = "lsl_stream_decrypted"
RECORDING_TIMER: int = 1000000
LED_SLEEP: bool = True

# start a recording session
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())


async def main():
    """
    This function is the main function for the script. It will start the recording and the LSL stream.
    """
    await asyncio.gather(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        ),
        stream_decrypted_data(bci.guardian_api),
    )


asyncio.run(main())
