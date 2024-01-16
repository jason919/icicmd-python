import json
from config import compartments
from config.ConfigReader import get_compartment_id
from loadbalancer import Backendset, Listener, Loadbalancer, Cert, RuleSet
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
Listener.add_new_header_listeners(
    "octa-uat-1b-lb.json",
    "octa-uat-1b-lb-internal",
    {
        "name": "HSTS",
        "items": [
            {
                "action": "ADD_HTTP_RESPONSE_HEADER",
                "header": "strict-transport-security",
                "value": "max-age=31536000",
            }
        ],
    },
)
# Backendset.update_backend_sets("octa-test-lb.json", "new-octa-test-lb", "SSO")
# Backendset.update_backend_sets("octa-training-lb.json", "new-octa-training-lb", "SSO")
# print(
#     Loadbalancer.get_ocid_from_new_load_balancer(
#         get_compartment_id("octa-prod"), "new-octa-prod-lb-internal"
#     )
# )
# Cert.update_expired_cert(
#     f"{os.getcwd()}/resources/oci/ssl/new",
#     "octa-uat-lb.json",
#     "internal",
#     "new-octa-uat-lb",
# )

# RuleSet.create(
#     "ocid1.compartment.oc1..aaaaaaaah2zzpsjuoihn6tg7plynb3jzbhwx67hgktddtk6dgmokkql5snxq",
#     "ocid1.loadbalancer.oc1.iad.aaaaaaaa74euhl5ft2onc2opyvnttqj7idgv47pwmo3uao2g6eldptruge6a",
#     {
#         "name": "HSTS",
#         "items": [
#             {
#                 "action": "ADD_HTTP_RESPONSE_HEADER",
#                 "header": "strict-transport-security",
#                 "value": "max-age=31536000",
#             }
#         ],
#     },
# )
