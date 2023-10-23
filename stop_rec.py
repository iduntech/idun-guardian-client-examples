"""
Sample script for using the Guardian Earbud Client
- To first stop existing recording manually in order to start a new recording
"""
import asyncio
from idun_guardian_client import GuardianClient
from idun_guardian_client.igeb_utils import stop_rec
from config import PASSWORD

stop_rec(
    device_id="XX-XX-XX-XX-XX-XX",
    recording_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    password=PASSWORD,
)
