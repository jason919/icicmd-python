from helper import OciHttpHelper


def create(compartment_id: str, load_balancer_ocid: str, post_json):
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "ruleSets", post_json, "POST"
    )


def fix_rules(compartment_id: str, load_balancer_ocid: str, rule_json):
    url = f"{OciHttpHelper.getLB_API_ENDPOINT()}/{load_balancer_ocid}/ruleSets?compartmentId={compartment_id}"
    OciHttpHelper.restCall(url, rule_json, "POST")


# [ADD_HTTP_REQUEST_HEADER, ADD_HTTP_RESPONSE_COOKIES_FLAGS, ADD_HTTP_RESPONSE_HEADER, ALLOW, CONTROL_ACCESS_USING_HTTP_METHODS, EXTEND_HTTP_REQUEST_HEADER_VALUE, EXTEND_HTTP_RESPONSE_HEADER_VALUE, HTTP_HEADER, IP_BASED_MAX_CONNECTIONS, REDIRECT, REMOVE_HTTP_REQUEST_HEADER, REMOVE_HTTP_RESPONSE_HEADER]

# https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets.htm#RequestResponsHeaderRules

# Adding headers to prevent external domains from iframing your site.

# Removing debug headers, such as "Server," sent by backend servers. This action helps you hide the implementation details of your backend.

# Adding the "strict-transport-security" header, with a proper value, to responses. This header helps guarantee that access to your site is HTTPS only.

# Adding the "x-xss-protection" header with a proper value. This header helps you enforce the cross-site scripting (XSS) protection built into modern browsers.

# Adding the "x-content-type" header with a proper value. This header helps you prevent attacks based on content type shifting.
