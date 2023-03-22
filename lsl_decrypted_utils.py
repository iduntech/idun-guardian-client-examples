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

    print("create LSL outlet")
    decrypted_outlet = configure_lsl_outlet(decrypted_data_model)

    while True:
        try:
            while True:
                if api_class.final_message_check:
                    break

                decrypted_package = await asyncio.wait_for(
                    api_class.decrypted_data_queue.get(), timeout=5.0
                )

                for idx, _ in enumerate(decrypted_package["timestamp"]):
                    sample = decrypted_package["ch1"][idx]
                    decrypted_outlet.push_sample([sample], local_clock())

                api_class.decrypted_data_queue.task_done()  # Notify receive_messages that we are done

            if api_class.final_message_check:
                break

        except Exception as lsl_error:
            logging_lsl_errors(lsl_error, api_class.debug)
            pass
    logging_ending_decryption(api_class.debug)


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

    name: str = "EEG_data"
    type: str = "EEG"
    channel_count: int = 1
    nominal_srate: int = 250
    channel_format: str = "float32"
    source_id: str = "EEG_data_id"
