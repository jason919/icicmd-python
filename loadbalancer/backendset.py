from helper.oci_http_helper import OCIHttpHelper


class BackendSet:
    @staticmethod
    def update(compartment_id, load_balancer_ocid, backend_set_name, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    f"backendSets/{backend_set_name}",
                                    post_json,
                                    "PUT")
