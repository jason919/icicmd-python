from helper.oci_http_helper import OCIHttpHelper


class Listener:
    @staticmethod
    def create(compartment_id, load_balancer_ocid, backend_set_name, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    "listeners",
                                    post_json,
                                    "POST")

    @staticmethod
    def update(compartment_id, load_balancer_ocid, listenerName, post_json):
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    f"listeners/{listenerName}",
                                    post_json,
                                    "PUT")
