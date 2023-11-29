import json
import os

current_dir = os.getcwd()
with open(f"{current_dir}/resources/oci/oci_config.json", "r") as oci_config_json_file:
    json_data = oci_config_json_file.read()

parsed_data = json.loads(json_data)

# Access the parsed data
compartments = parsed_data["compartments"]

orb_certs = {}
octa_certs = {}
self_dev_certs = {}
self_prod_certs = {}

with open(f"{current_dir}/resources/oci/ssl/orb/ca.crt", "r") as orb_ca_file:
    orb_certs["ca"] = orb_ca_file.read()
with open(f"{current_dir}/resources/oci/ssl/orb/public.pem", "r") as orb_pub_file:
    orb_certs["public"] = orb_pub_file.read()
with open(f"{current_dir}/resources/oci/ssl/orb/private.pem", "r") as orb_pri_file:
    orb_certs["private"] = orb_pri_file.read()

with open(f"{current_dir}/resources/oci/ssl/octa/ca.crt", "r") as octa_ca_file:
    octa_certs["ca"] = octa_ca_file.read()
with open(f"{current_dir}/resources/oci/ssl/octa/public.pem", "r") as octa_pub_file:
    octa_certs["public"] = octa_pub_file.read()
with open(f"{current_dir}/resources/oci/ssl/octa/private.pem", "r") as octa_pri_file:
    octa_certs["private"] = octa_pri_file.read()

with open(f"{current_dir}/resources/oci/ssl/octa/405/ca.crt", "r") as octa_pri_file:
    octa_certs["ca-405"] = octa_pri_file.read()
with open(f"{current_dir}/resources/oci/ssl/octa/405/public.pem", "r") as octa_pri_file:
    octa_certs["public-405"] = octa_pri_file.read()
with open(f"{current_dir}/resources/oci/ssl/octa/405/private.pem", "r") as octa_pri_file:
    octa_certs["private-405"] = octa_pri_file.read()

with open(f"{current_dir}/resources/oci/ssl/self/self-public.pem", "r") as self_dev_pub_file:
    self_dev_certs["public"] = self_dev_pub_file.read()
with open(f"{current_dir}/resources/oci/ssl/self/self-private.pem", "r") as self_dev_pri_file:
    self_dev_certs["private"] = self_dev_pri_file.read()

with open(f"{current_dir}/resources/oci/ssl/self/orb-prod-public.pem",
          "r") as self_orb_prod_pub_file:
    self_prod_certs["orb-public"] = self_orb_prod_pub_file.read()
with open(f"{current_dir}/resources/oci/ssl/self/orb-prod-private.pem",
          "r") as self_orb_prod_pri_file:
    self_prod_certs["orb-private"] = self_orb_prod_pri_file.read()

with open(f"{current_dir}/resources/oci/ssl/self/octa-prod-public.pem",
          "r") as self_octa_prod_pub_file:
    self_prod_certs["octa-public"] = self_octa_prod_pub_file.read()
with open(f"{current_dir}/resources/oci/ssl/self/octa-prod-private.pem",
          "r") as self_octa_prod_pri_file:
    self_prod_certs["octa-private"] = self_octa_prod_pri_file.read()
