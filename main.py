from config import compartments
from loadbalancer import Backendset, Listener, Loadbalancer

# Loadbalancer.update_backend_sets('octa-training/create-octa-lb-new.json')
# Loadbalancer.list_loadbalancer()
# Loadbalancer.update_display_name(
#     compartments["octa-uat"],
#     "ocid1.loadbalancer.oc1.iad.aaaaaaaajgko2vqbqp5kq6ifhysov3lva2kfel6bhymo2qilnn535dq3kpda",
#     "new-octa-uat-lb-public",
# )
Loadbalancer.backup_all_loadbalancers()
# Backendset.print_all_ip_port()
# Listener.update_listeners("octa-test-lb.json", "new-octa-test-lb")
# Backendset.update_backend_sets("octa-test-lb.json", "new-octa-test-lb", "SSO")
