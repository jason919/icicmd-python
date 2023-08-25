import json
import os
import time
from helper import JsonHelper, OciHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "listeners", post_json, "POST"
    )


def update(compartment_id: str, load_balancer_ocid: str, listener_name: str, post_json):
    OciHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"listeners/{listener_name}",
        post_json,
        "PUT",
    )


def update_listeners(
    json_file_name: str, load_balancer_name: str, listener_name: str = ""
):
    with open(
        f"{os.getcwd()}/resources/files/saved/{json_file_name}", "r"
    ) as json_file:
        json_text = json_file.read()

    parsed_data = JsonHelper.get_lb_data_from_compartment_json(
        json_text, load_balancer_name
    )
    compartment_id = parsed_data["compartmentId"]
    load_balancer_ocid = parsed_data["id"]
    listeners = parsed_data["listeners"]
    for key, value in listeners.items():
        print(key)
        if listener_name == "" or listener_name == key:
            update(compartment_id, load_balancer_ocid, str(key), value)
            time.sleep(20)


def update_listeners_with_cert_name(
    compartment_id: str, load_balancer_ocid: str, parsed_data, cert_name: str
):
    listeners = parsed_data["listeners"]
    for key, value in listeners.items():
        print(key)
        value["sslConfiguration"]["certificateName"] = cert_name
        update(compartment_id, load_balancer_ocid, str(key), value)
        time.sleep(20)
