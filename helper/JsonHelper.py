import json


def get_lb_data_from_compartment_json(json_text: str, load_balancer_name: str):
    for _lb_data in json.loads(json_text):
        if _lb_data["displayName"] == load_balancer_name:
            return _lb_data
