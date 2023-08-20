from helper.oci_http_helper import OCIHttpHelper


class Hostname:
    @staticmethod
    def create(compartment_id, load_balancer_ocid, backend_set_name, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    "hostnames",
                                    post_json,
                                    "POST")
