"""Function used to list all the metadata associated to a specific Recording"""
import asyncio
from datetime import datetime
from idun_data_models import (
    Metadata_in,
    Metadata_out,
    Marker,
    MAX_MARKER_COUNT,
)
from config import PASSWORD
from idun_guardian_client.igeb_metadata import MetadataClient

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"

LIMIT: int = 100  # Define here the Number of elements to return in 1 request (limit)-> default = 3.
CURSOR: int = 1  # Define, if needed, the id value of the last element in the previous query to choose from where to take new metadata (cursor)

client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)

metadata_list = asyncio.run(
    client.list_metadata(
        params={
            "limit": LIMIT,
            # "cursor": CURSOR,
        },
    )
)

print(f"Listing the metadata associated to the recording ID {RECORDING_ID}")
for en, metadata in enumerate(metadata_list):
    print(f"Metadata ID: {metadata.id} : {metadata}\n")
