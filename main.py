import json
from config import compartments
from config.ConfigReader import get_compartment_id
from loadbalancer import Backendset, Listener, Loadbalancer, Cert
import os

# Loadbalancer.create_single_loadbalancer(
#     "test.json", "lb_test", get_compartment_id("octa-prod")
# )
# Loadbalancer.create_single_loadbalancer(
#     "octa-dr-lb-new.json", "new-octa-dr-online-public", get_compartment_id("octa-dr")
# )

# with open(
#     "C:/drive-d/projects/etcc/company/CICD/ocicmd-python/resources/files/saved/octa-dr-lb-new.json",
#     "r",
# ) as json_file:
#     post_json = json.loads(json_file.read())
# Loadbalancer.create_all_loadbalancer(get_compartment_id("octa-dr"), post_json)

# Loadbalancer.update_backend_sets('octa-training/create-octa-lb-new.json')
# Loadbalancer.list_loadbalancer()
# Loadbalancer.update_display_name(
#     compartments["octa-uat"],
#     "ocid1.loadbalancer.oc1.iad.aaaaaaaajgko2vqbqp5kq6ifhysov3lva2kfel6bhymo2qilnn535dq3kpda",
#     "octa-uat-iva-public",
# )
# Loadbalancer.backup_all_loadbalancers()
# Backendset.print_all_ip_port()
# Listener.update_listeners("octa-test-lb.json", "new-octa-test-lb")
# Backendset.update_backend_sets("octa-test-lb.json", "new-octa-test-lb", "SSO")
# Backendset.update_backend_sets("octa-training-lb.json", "new-octa-training-lb", "SSO")
# print(
#     Loadbalancer.get_ocid_from_new_load_balancer(
#         get_compartment_id("octa-prod"), "new-octa-prod-lb-internal"
#     )
# )
Cert.update_expired_cert(
    f"{os.getcwd()}/resources/oci/ssl/orb",
    "orb-training-lb.json",
    "LB",
    "orb-training-lb-internal",
)
