import json
import os
import time
from helper import OciHttpHelper


def update(
    compartment_id: str, load_balancer_ocid: str, backend_set_name: str, post_json
):
    OciHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"backendSets/{backend_set_name}",
        post_json,
        "PUT",
    )


def update_backend_sets(json_file_name: str, load_balancer_name: str):
    with open(
        f"{os.getcwd()}/resources/files/saved/{json_file_name}", "r"
    ) as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)[load_balancer_name]
    compartment_id = parsed_data["compartmentId"]
    load_balancer_ocid = parsed_data["id"]
    backend_sets = parsed_data["backendSets"]
    for key, value in backend_sets.items():
        print(key)
        update(compartment_id, load_balancer_ocid, key, value)
        time.sleep(20)


def update_backend_sets_with_cert_name(
    compartment_id: str, load_balancer_ocid: str, parsed_data, cert_name: str
):
    backend_sets = parsed_data["backendSets"]
    for key, value in backend_sets.items():
        print(key)
        value["sslConfiguration"]["certificateName"] = cert_name
        update(compartment_id, load_balancer_ocid, key, value)
        time.sleep(20)


def print_all_ip_port():
    directory_path = f"{os.getcwd()}/resources/files/saved"
    print(directory_path)
    file_list = sorted(os.listdir(directory_path))
    for filename in file_list:
        if os.path.isfile(os.path.join(directory_path, filename)):
            if ".json" in filename and "Deleted" not in filename:
                print(f"\n\n{filename}")
                with open(os.path.join(directory_path, filename), "r") as json_file:
                    json_data = json_file.read()
                    if len(json_data) > 500:
                        parsed_data = json.loads(json_data)
                        for _lb in parsed_data:
                            _backend_sets = _lb["backendSets"]
                            # print(f"LB name: {_lb['displayName']}")
                            for key, value in _backend_sets.items():
                                if len(value["backends"]) > 0:
                                    print(f"{key}: {value['backends'][0]['name']}")
                                else:
                                    print(f"{key}: {value['backends']}")
