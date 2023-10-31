import json


def get_lb_data_from_compartment_json(json_text: str, load_balancer_name: str):
    for _lb_data in json.loads(json_text):
        if _lb_data["displayName"] == load_balancer_name:
            return _lb_data


def get_lb_names_from_compartment_json(json_text: str):
    lb_names = []
    for _lb_data in json.loads(json_text):
        lb_names.append(_lb_data["displayName"])
    return lb_names
