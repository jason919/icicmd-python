import json
from config import compartments
from config.ConfigReader import get_compartment_id
from loadbalancer import Backendset, Listener, Loadbalancer

# Loadbalancer.create_loadbalancer(
#     "test.json", "lb_test", get_compartment_id("octa-prod")
# )
# Loadbalancer.create_loadbalancer(
#     "octa-prod-lb.json", "new-octa-prod-lb", get_compartment_id("octa-prod")
# )
# with open(
#     "C:/drive-d/projects/etcc/company/CICD/icicmd-python/resources/files/saved/test3.json",
#     "r",
# ) as json_file:
#     post_json = json.loads(json_file.read())
# Loadbalancer.create(get_compartment_id("octa-prod"), post_json)

# Loadbalancer.update_backend_sets('octa-training/create-octa-lb-new.json')
# Loadbalancer.list_loadbalancer()
# Loadbalancer.update_display_name(
#     compartments["octa-uat"],
#     "ocid1.loadbalancer.oc1.iad.aaaaaaaajgko2vqbqp5kq6ifhysov3lva2kfel6bhymo2qilnn535dq3kpda",
#     "octa-uat-iva-public",
# )
Loadbalancer.backup_all_loadbalancers()
# Backendset.print_all_ip_port()
# Listener.update_listeners("octa-test-lb.json", "new-octa-test-lb")
# Backendset.update_backend_sets("octa-test-lb.json", "new-octa-test-lb", "SSO")
# Backendset.update_backend_sets("octa-training-lb.json", "new-octa-training-lb", "SSO")
# print(
#     Loadbalancer.get_ocid_from_new_load_balancer(
#         get_compartment_id("octa-prod"), "new-octa-prod-lb-internal"
#     )
# )
