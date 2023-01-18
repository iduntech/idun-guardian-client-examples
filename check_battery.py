import asyncio
from idun_guardian_client import GuardianClient

# Get device address
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())

# start a impedance session
asyncio.run(bci.start_battery())
