import asyncio
from idun_guardian_client import GuardianClient


EXPERIMENT: str = "Sleeping"
RECORDING_TIMER: int = 36000  # 10 hours in seconds
LED_SLEEP: bool = False
SENDING_TIMEOUT: float = 2 # If no receipt is received for 2 seconds, the data is buffered
                           # If you experience excessive disruptions, try increasing this value
BI_DIRECTIONAL_TIMEOUT: float = 20  # If no bi-directional data is received for 20 seconds, the connection is re-established
                                    # If you experience excessive disruptions, try increasing this value

# start a recording session
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())

# start a recording session
asyncio.run(
    bci.start_recording(
        recording_timer=RECORDING_TIMER,
        led_sleep=LED_SLEEP,
        experiment=EXPERIMENT,
        sending_timout=SENDING_TIMEOUT,
        bi_directional_receiving_timeout=BI_DIRECTIONAL_TIMEOUT,
    )
)