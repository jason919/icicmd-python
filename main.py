from helper import LoadBalancerManager
from config import compartments
from loadbalancer import Loadbalancer

# LoadBalancerManager.update_backend_sets('octa-training/create-octa-lb-new.json')
# LoadBalancerManager.list_loadbalancer()
Loadbalancer.update_display_name(
    compartments["octa-uat"],
    "ocid1.loadbalancer.oc1.iad.aaaaaaaajgko2vqbqp5kq6ifhysov3lva2kfel6bhymo2qilnn535dq3kpda",
    "new-octa-only-uat-lb",
)
