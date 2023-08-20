import json
import os
import time

from config import orb_certs
from config.config_reader import get_compartment_id
from loadbalancer import Cert, RouteSet, Listener, Backendset, Loadbalancer


def backup_loadbalancer():
    print('start backup')
    compartment_id = get_compartment_id('octa-dev')
    print(compartment_id)
    print(orb_certs['ca'])
    return


def update_backend_sets(json_file_name: str):
    current_dir = os.getcwd()
    with open(f'{current_dir}/files/create/{json_file_name}', 'r') as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)
    compartment_id = parsed_data['compartmentId']
    load_balancer_ocid = parsed_data['id']
    backend_sets = parsed_data['backendSets']
    for key, value in backend_sets.items():
        print(key)
        Backendset.update(compartment_id, load_balancer_ocid, key, value)
        time.sleep(20)


def update_listeners(json_file_name: str):
    current_dir = os.getcwd()
    with open(f'{current_dir}/files/create/{json_file_name}', 'r') as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)
    compartment_id = str(parsed_data['compartmentId'])
    load_balancer_ocid = str(parsed_data['id'])
    listeners = parsed_data['listeners']
    for key, value in listeners.items():
        print(key)
        Listener.update(compartment_id, load_balancer_ocid, str(key), value)
        time.sleep(20)


def create_loadbalancer(json_file_name: str):
    with open(f'{os.getcwd()}/files/create/{json_file_name}', 'r') as json_file:
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
        ocid = Loadbalancer.get_ocid_from_new_load_balancer(compartment_id, load_balancer_name)
        print(f"new ocid: {ocid}")
        for value in routing_policies.values():
            RouteSet.create(compartment_id, ocid, value)
        time.sleep(30)
        for value in json.loads(listeners_backup).values():
            Listener.create(compartment_id, ocid, value)
