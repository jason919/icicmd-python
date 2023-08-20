from config import compartments


def get_compartment_id(compartment_name: str):
    return compartments[compartment_name]
