"""Function used to list all the metadata associated to a specific Recording"""
import asyncio

from config import PASSWORD
from idun_guardian_client.igeb_metadata import MetadataClient

META_DATA_ID = "19"  # "<the_metadata_id_associated_to_the_recording_id>", this is important to get the right meta data corresponding to your recording

DEVICE_ID = "XX-XX-XX-XX-XX-XX"  # "<your_device_ID> ex:"XX-XX-XX-XX-XX-XX""
RECORDING_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # "<the_recording_id>"  ex: "py-e852d8d6-9235-4b4b-95a9-7a30f1076f55"

LIMIT: int = 10  # Define here the Number of elements to return in 1 request (limit)-> default = 3.
CURSOR: int = 0  # Define, if needed, the id value of the last element in the previous query to choose from where to take new metadata (cursor)


client = MetadataClient(DEVICE_ID, RECORDING_ID, PASSWORD)
markers_list = asyncio.run(client.get_markers(META_DATA_ID, params={"limit": LIMIT}))

for en, metadata in enumerate(markers_list):
    print(f"Listing the metadata associated to the recording ID {RECORDING_ID}")
    print(f"Metadata number {en} : {metadata}\n")
