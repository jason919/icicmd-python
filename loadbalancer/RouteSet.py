from helper import lb_api_endpoint
from helper import OciHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "routingPolicies", post_json, "POST"
    )


def fix_routes(compartment_id: str, load_balancer_ocid: str, route_json):
    url = f"{lb_api_endpoint}/{load_balancer_ocid}/routingPolicies?compartmentId={compartment_id}"
    response = OciHttpHelper.restCall(url, route_json, "POST")
