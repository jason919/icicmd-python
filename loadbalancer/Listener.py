import json
import os
import time
from helper import OciHttpHelper


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


def update_listeners(json_file_name: str):
    with open(f"{os.getcwd()}/files/create/{json_file_name}", "r") as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)
    compartment_id = str(parsed_data["compartmentId"])
    load_balancer_ocid = str(parsed_data["id"])
    listeners = parsed_data["listeners"]
    for key, value in listeners.items():
        print(key)
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
