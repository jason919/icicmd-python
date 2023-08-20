import json
import os
import time

from config import orb_certs
from config.config_reader import ConfigReader
from loadbalancer.backendset import BackendSet


class LoadBalancerManager:
    @staticmethod
    def backup_loadbalancer():
        print('start backup')
        compartment_id = ConfigReader.get_compartment_id('octa-dev')
        print(compartment_id)
        print(orb_certs['ca'])
        return

    @staticmethod
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
            BackendSet.update(compartment_id, load_balancer_ocid, key, value)
            time.sleep(20)
