import asyncio
from idun_guardian_client import GuardianClient


EXPERIMENT: str = "Sleeping"
RECORDING_TIMER: int = 36000  # 10 hours in seconds
LED_SLEEP: bool = False
SENDING_TIMEOUT: float = 2 # If you experience disruptions, try increasing this value
BI_DIRECTIONAL_TIMEOUT: float = 20  # If you experience disruptions, try increasing this value

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