"""Example Function used to post new metadata for a Recording"""
import asyncio
import numpy as np
from datetime import datetime
from idun_data_models import (
    Metadata_in,
    Marker,
)
from config import PASSWORD
from idun_guardian_client.igeb_metadata import MetadataClient

# If you run this script, meta data will be created aas well as markers and it will be associated with the returned meta data ID

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"
DISPLAY_NAME: str | None = "last_test"  # This will be an additional name for the metadata, you have the freedom to choose it
EXPERIMENT_NAME: str = "nap"  # This can only be according to the Metadata_in enum class, you can find the list of possible values in the idun_data_models.rest_metadata.py file

MARKERS = [
    Marker(
        timestamp=datetime.now(), marker={"last_sleep_event": np.random.randint(10)}
    )  # This is an example of a marker, you can add up to a 1000
    for _ in range(100)
]

# You can send only the markers, only the metadata or both;
# in case you want to send just one of them please comments on the variable definition(metadata_dictionary_toSend, markers_toSend)
# and/or comment the metadata or markers parameters passed on the Metadata_in object in the request function below
client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)
metadata_markers = asyncio.run(
    client.create_metadata(
        Metadata_in(
            displayName=DISPLAY_NAME,
            experiment_name=EXPERIMENT_NAME,
            markers=MARKERS,
        ),
    )
)
print(
    f"Succesfully created the metadata:\n{metadata_markers} with metadata ID: {metadata_markers.id}"
)
