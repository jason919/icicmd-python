from config import compartments
from helper import OciHttpHelper


def get_compartment_id(compartment_name: str):
    if "-dr" in compartment_name:
        OciHttpHelper.setDr(True)
    else:
        OciHttpHelper.setDr(False)
    return compartments[compartment_name]
