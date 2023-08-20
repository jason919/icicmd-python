import json
import os

current_dir = os.getcwd()
with open(f'{current_dir}/resources/oci/oci_config.json', 'r') as oci_config_json_file:
    json_data = oci_config_json_file.read()

parsed_data = json.loads(json_data)

# Access the parsed data
compartments = parsed_data['compartments']

orb_certs = {}
octa_certs = {}
self_dev_certs = {}
self_prod_certs = {}

with open(f'{current_dir}/resources/oci/ssl/orb/ca.crt', 'r') as orb_ca_file:
    orb_certs['ca'] = orb_ca_file.read()
with open(f'{current_dir}/resources/oci/ssl/orb/public.pem', 'r') as orb_pub_file:
    orb_certs['pubic'] = orb_pub_file.read()
with open(f'{current_dir}/resources/oci/ssl/orb/private.pem', 'r') as orb_pri_file:
    orb_certs['private'] = orb_pri_file.read()

with open(f'{current_dir}/resources/oci/ssl/octa/ca.crt', 'r') as octa_ca_file:
    octa_certs['ca'] = octa_ca_file.read()
with open(f'{current_dir}/resources/oci/ssl/octa/public.pem', 'r') as octa_pub_file:
    octa_certs['pubic'] = octa_pub_file.read()
with open(f'{current_dir}/resources/oci/ssl/octa/private.pem', 'r') as octa_pri_file:
    octa_certs['private'] = octa_pri_file.read()

with open(f'{current_dir}/resources/oci/ssl/self/dev1-public.pem', 'r') as self_dev_pub_file:
    self_dev_certs['pubic'] = self_dev_pub_file.read()
with open(f'{current_dir}/resources/oci/ssl/self/dev1-private.pem', 'r') as self_dev_pri_file:
    self_dev_certs['private'] = self_dev_pri_file.read()

with open(f'{current_dir}/resources/oci/ssl/self/prod-public.pem', 'r') as self_prod_pub_file:
    self_prod_certs['pubic'] = self_prod_pub_file.read()
with open(f'{current_dir}/resources/oci/ssl/self/prod-private.pem', 'r') as self_prod_pri_file:
    self_prod_certs['private'] = self_prod_pri_file.read()
