from helper import OCIHttpHelper


def update(
    compartment_id: str, load_balancer_ocid: str, backend_set_name: str, post_json
):
    OCIHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"backendSets/{backend_set_name}",
        post_json,
        "PUT",
    )