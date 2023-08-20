from config import compartments


class ConfigReader:
    @staticmethod
    def get_compartment_id(compartment_name: str):
        return compartments[compartment_name]
