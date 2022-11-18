from idun_guardian_client_beta.igeb_api import GuardianAPI

api = GuardianAPI()

# download recording
api.download_recording_by_id(
    device_id = "XX-XX-XX-XX-XX-XX",
    recording_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
)
# The info about th recording can be found in the log file