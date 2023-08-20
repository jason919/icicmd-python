from helper import lb_api_endpoint
from helper import OCIHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OCIHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "routingPolicies", post_json, "POST"
    )


def fix_routes(compartment_id: str, load_balancer_ocid: str, route_json):
    url = f"{lb_api_endpoint}/{load_balancer_ocid}/routingPolicies?compartmentId={compartment_id}"
    response = OCIHttpHelper.restCall(url, route_json, "POST")
