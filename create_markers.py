"""Example Function used to create new markers for a  specific metadata"""
import asyncio
import numpy as np
from datetime import datetime
from idun_data_models.rest_metadata import (
    Marker,
)
from config import PASSWORD
from idun_guardian_client.igeb_metadata import MetadataClient

# IMPORTANT: Only use this example if you want to add new markers to an existing metadata ID, so you need to have added meta data to the recording
# You have to run create_metadata.py first to create a new metadata and then run this script to add markers to it

META_DATA_ID = "19"  # "<the_metadata_id_associated_to_the_recording_id>", it is important to know your meta data ID to add markers to it

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"
# If the META_DATA_ID does not exist, first create a new metadata using the create_metadata.py example
# If the META_DATA_ID does exist and you have not added markers, then the markers will be added
# If the META_DATA_ID does exist and you have already added markers, then the markers will be added to the existing ones at the end

MARKERS = [
    Marker(timestamp=datetime.now(), marker={"sleepy": np.random.randint(10)})
    for _ in range(100)
]

client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)
response = asyncio.run(client.create_markers(META_DATA_ID, MARKERS))

if response:
    print(
        f"Successfully add to the the metadata ID '{META_DATA_ID}'"
        f" associated with the recording ID '{RECORDING_ID}'"
        f" the following marker:\n{MARKERS}"
    )
