from helper import LbApiEndpoint
from helper.oci_http_helper import OCIHttpHelper


class RouteSet:
    @staticmethod
    def create(compartment_id: str, load_balancer_ocid: str, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    "routingPolicies",
                                    post_json,
                                    "POST")

    @staticmethod
    def fix_routes(compartment_id: str, load_balancer_ocid: str, route_json):
        url = f"{LbApiEndpoint}/{load_balancer_ocid}/routingPolicies?compartmentId={compartment_id}"
        response = OCIHttpHelper.restCall(url,
                                          route_json,
                                          "POST")
