import asyncio
from idun_guardian_client_beta import GuardianClient


EXPERIMENT: str = "Sleeping"
RECORDING_TIMER: int = 5000 # 10 hours in seconds
LED_SLEEP: bool = False

# start a recording session
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())

# start a recording session
asyncio.run(
    bci.start_recording(
        recording_timer=RECORDING_TIMER,
        led_sleep=LED_SLEEP,
        experiment=EXPERIMENT
    )
)