from helper import OciHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "routingPolicies", post_json, "POST"
    )


def fix_routes(compartment_id: str, load_balancer_ocid: str, route_json):
    url = f"{OciHttpHelper.getLB_API_ENDPOINT()}/{load_balancer_ocid}/routingPolicies?compartmentId={compartment_id}"
    OciHttpHelper.restCall(url, route_json, "POST")
