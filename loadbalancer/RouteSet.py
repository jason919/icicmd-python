from helper import LbApiEndpoint
from helper.oci_http_helper import OCIHttpHelper


class RouteSet:
    @staticmethod
    def create(compartment_id, load_balancer_ocid, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    "routingPolicies",
                                    post_json,
                                    "POST")

    @staticmethod
    def fix_routes(compartment_id, load_balancer_ocid, load_balancer_name, route_json):
        url = f"{LbApiEndpoint}/{load_balancer_ocid}/routingPolicies?compartmentId={compartment_id}"
        response = OCIHttpHelper.restCall(url,
                                          route_json,
                                          "POST")
