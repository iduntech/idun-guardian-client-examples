from idun_guardian_client_beta.igeb_api import GuardianAPI

api = GuardianAPI()

# get single recording
api.get_recording_info_by_id(
    device_id = "XX-XX-XX-XX-XX-XX",
    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
)