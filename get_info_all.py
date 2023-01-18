from idun_guardian_client.igeb_api import GuardianAPI

api = GuardianAPI()

# get a list of all recordings
recording_list = api.get_recordings_info_all(
    device_id="XX-XX-XX-XX-XX-XX"
)  # Device ID is derived from the MAC address of the earbud and in the log file
