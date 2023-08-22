import json
import os
import time

from helper import LB_API_ENDPOINT
from helper import OciHttpHelper
from config import orb_certs, compartments
from config.ConfigReader import get_compartment_id
from loadbalancer import Cert, RouteSet, Listener, Loadbalancer


def create(compartment_id: str, post_json):
    print("start LoadBalancer create 1")
    url = f"{LB_API_ENDPOINT}?compartmentId={compartment_id}"
    OciHttpHelper.restCall(url, post_json, "POST")


def update_display_name(compartment_id: str, ocid: str, new_name: str):
    print("start update_loadbalancer_display_name 1")
    url = f"{LB_API_ENDPOINT}/{ocid}?compartmentId={compartment_id}"
    post_json = {"displayName": new_name}
    OciHttpHelper.restCall(url, post_json, "PUT")


def list_load_balancers(compartment_id: str) -> str:
    url = f"{LB_API_ENDPOINT}?compartmentId={compartment_id}"
    return OciHttpHelper.restGet(url)


def backup(compartment_name: str, compartment_id: str):
    text = list_load_balancers(compartment_id)
    if len(text) > 100:
        file_path = f"{os.getcwd()}/files/saved/{compartment_name}-lb.json"
        with open(file_path, "w") as file:
            file.write(text)
    else:
        print(f"the compartment {compartment_name} has no data")


def get_ocid_from_new_load_balancer(
    compartment_id: str, load_balancer_display_name: str
) -> str:
    for i in range(0, 5):
        all_load_balancers_json = json.loads(list_load_balancers(compartment_id))
        ocid: str = ""
        state: str = ""
        for value in all_load_balancers_json.values():
            if value["displayName"] == load_balancer_display_name:
                ocid = value["id"]
                state = value["lifecycleState"]
                break
        if len(ocid) > 10 and state == "ACTIVE":
            return ocid
        else:
            time.sleep(15)
    return ""


def list_loadbalancer():
    print(Loadbalancer.list_load_balancers(compartments["orb-dev"]))


def backup_loadbalancer():
    print("start backup")
    compartment_id = get_compartment_id("octa-dev")
    print(compartment_id)
    print(orb_certs["ca"])
    return


def create_loadbalancer(json_file_name: str):
    with open(f"{os.getcwd()}/files/create/{json_file_name}", "r") as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)
    load_balancer_name = parsed_data["displayName"]
    compartment_id = parsed_data["compartmentId"]
    certificates = parsed_data["certificates"]
    Cert.fix_certs_in_creation_json(certificates)
    routing_policies = parsed_data["routingPolicies"]

    listeners_backup = None
    if len(json.dumps(routing_policies)) > 10:
        listeners_backup = parsed_data["listeners"]
        parsed_data["listeners"] = []
    Loadbalancer.create(compartment_id, parsed_data)

    if len(json.dumps(routing_policies)) > 10:
        print("wait for the load balancer is created, then fix the routes")
        time.sleep(30)
        ocid = Loadbalancer.get_ocid_from_new_load_balancer(
            compartment_id, load_balancer_name
        )
        print(f"new ocid: {ocid}")
        for value in routing_policies.values():
            RouteSet.create(compartment_id, ocid, value)
        time.sleep(30)
        for value in json.loads(listeners_backup).values():
            Listener.create(compartment_id, ocid, value)
