from pylsl import StreamInfo, StreamOutlet, local_clock
import asyncio
import logging
import json
from dataclasses import dataclass, asdict
import datetime


async def stream_decrypted_data(api_class):
    """Send data to the LSL stream

    Args:
        decrypted_data_queue (asyncio.Queue): Queue containing decrypted data

    Returns:
        None
    """
    decrypted_data_model = GuardianDecryptedModel()
    logging_lsl_data_model(GuardianDecryptedModel, True)
    while True:
        try:
            decrypted_outlet = configure_lsl_outlet(decrypted_data_model)
            while True:
                if api_class.final_message_check:
                    break
                decrypted_package = await asyncio.wait_for(
                    api_class.decrypted_data_queue.get(), timeout=5.0
                )
                sample = decrypted_package[1]
                # Find the timestamp of the original package
                lsl_time_original = calculate_original_lsl_timestamp(
                    decrypted_package[0]
                )
                decrypted_outlet.push_sample([sample], lsl_time_original)
            if api_class.final_message_check:
                break
        except Exception as lsl_error:
            logging_lsl_errors(lsl_error, api_class.debug)
    logging_ending_decryption(api_class.debug)


def calculate_original_lsl_timestamp(original_package_timestamp):
    """Calculate the original LSL timestamp

    Args:
        original_package_timestamp (float):  Timestamp of the original package in seconds from 1970,1,1

    Returns:
        float: Original LSL timestamp in seconds and LSL referenced time
    """
    # Find the current timestamp using same format as the original package timestamp
    current_timestamp = float(
        datetime.datetime.fromisoformat(
            datetime.datetime.now().astimezone().isoformat()
        ).timestamp()
    )
    # calculate the difference or error between the the original package timestamp and the current timestamp
    difference_to_current_time = current_timestamp - original_package_timestamp
    # Calculate the LSL timestamp
    lsl_time_current = local_clock()
    # Calculate the LSL timestamp of the original package by removing the difference or error to the current time
    lsl_time_original = lsl_time_current - difference_to_current_time
    return lsl_time_original


def configure_lsl_outlet(datamodel):
    """Configure the LSL outlet

    Args:
        datamodel (DataModel): Data model to be streamed

    Returns:
        StreamOutlet: LSL outlet

    """
    data_outlet = StreamOutlet(
        StreamInfo(
            name=datamodel.name,
            type=datamodel.type,
            channel_count=datamodel.channel_count,
            nominal_srate=datamodel.nominal_srate,
            channel_format=datamodel.channel_format,
            source_id=datamodel.source_id,
        )
    )
    return data_outlet


def logging_lsl_data_model(GuardianDecryptedModel, debug):
    if debug:
        logging.info(
            "[API] Decrypted LSL data model: %s",
            json.dumps(asdict(GuardianDecryptedModel()), indent=4),
        )


def logging_lsl_errors(error, debug):
    if debug:
        logging.info("[API]: Warning in LSL stream: %s", error)


def logging_ending_decryption(debug):
    if debug:
        logging.info("[API] ----------- Decrypted LSL stream COMPLETED -----------")


@dataclass
class GuardianDecryptedModel:
    """Data model for Guardian data"""

    name: str = "Decrypted_EEG_IMU"
    type: str = "Decrypted_EEG_IMU"
    channel_count: int = 1
    nominal_srate: int = 0
    channel_format: str = "float32"
    source_id: str = "Decrypted_EEG_data_id"
