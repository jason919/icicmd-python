from helper import OCIHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OCIHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "listeners", post_json, "POST"
    )


def update(compartment_id: str, load_balancer_ocid: str, listener_name: str, post_json):
    OCIHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"listeners/{listener_name}",
        post_json,
        "PUT",
    )
