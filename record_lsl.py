"""
Sample script for using the Guardian Earbud Client
- Start recording data from the Guardian Earbuds
"""
import asyncio
from idun_guardian_client.client import GuardianClient
from lsl_utils import stream_data

EXPERIMENT: str = "lsl_stream"
RECORDING_TIMER: int = 1000000
LED_SLEEP: bool = True
SENDING_TIMEOUT: float = 2  # If you experience disruptions, try increasing this value
BI_DIRECTIONAL_TIMEOUT: float = 4  # If you experience disruptions, try increasing this value

# start a recording session
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())


async def main():
    """
    This function is the main function for the script. It will start the recording and the LSL stream.
    """
    await asyncio.gather(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
            experiment=EXPERIMENT,
            sending_timout=SENDING_TIMEOUT,
            bi_directional_receiving_timeout=BI_DIRECTIONAL_TIMEOUT,
        ),
        stream_data(bci.guardian_api),
    )


asyncio.run(main())
