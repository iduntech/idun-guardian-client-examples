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

# You can run this file and it will create a new metadata and it will be associated with the returned meta data ID

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"
DISPLAY_NAME: str | None = "test"
EXPERIMENT_NAME = "nap"

# You can send only the markers, only the metadata or both;
# in case you want to send just one of them please comments on the variable definition(metadata_dictionary_toSend, markers_toSend)
# and/or comment the metadata or markers parameters passed on the Metadata_in object in the request function below
client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)
metadata_markers = asyncio.run(
    client.create_metadata(
        Metadata_in(
            displayName=DISPLAY_NAME,
            experiment_name=EXPERIMENT_NAME,
        ),
    )
)
print(
    f"Succesfully created the metadata:\n{metadata_markers} with Meta Data ID: {metadata_markers.id}"
)
