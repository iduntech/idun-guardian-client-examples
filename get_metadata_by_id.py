"""Function used to get a metadata for a Recording
   If to_save == True the metadata is stored at the specified path"""
import asyncio
import os
from config import PASSWORD
from idun_guardian_client.igeb_metadata import MetadataClient

# Define here all the metadataID you want to get associated to the same recordingID
META_DATA_ID = "19"  # "<the_metadata_id_associated_to_the_recording_id>", this is important to get the right meta data corresponding to your recording

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"

client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)
markers_list = asyncio.run(client.get_metadata(META_DATA_ID))

print(f"Listing the metadata associated to the recording ID {RECORDING_ID}")
for en, metadata in enumerate(markers_list):
    # print the key and the value in the metadata
    print(f"{metadata}\n")
