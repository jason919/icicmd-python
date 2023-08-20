# oci_http_helper.py
import json
import time

import requests

from helper import lb_api_endpoint, auth


def restGet(url: str):
    # headers = {
    #     'Date': datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')
    # }
    response = requests.get(url, auth=auth)
    # response.raise_for_status()
    print(f"response code: {response.status_code}")
    if response.status_code != 200:
        print(f"restCall error body, {response.text}")
    return response.text


def restCall(url: str, body, method: str):
    # headers = {
    #     'Date': datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z'),
    #     'content-type': 'application/json'
    # }
    # print(body)
    # prepared_request = requests.Request(method, url, json=body,
    #                                     auth=auth).prepare()
    #
    # print("Outgoing Headers:")
    # for key, value in prepared_request.headers.items():
    #     print(f"{key}: {value}")
    # auth.validate_request(prepared_request)
    # response = requests.Session().send(prepared_request)
    if method == 'POST':
        response = requests.post(url, json.dumps(body), auth=auth)
    else:
        response = requests.put(url, json.dumps(body), auth=auth)
        # response.raise_for_status()
    print(f"response code: {response.status_code}")
    if response.status_code != 204:
        print(f"restCall error body, {response.text}")
    return response


def retryRestCall(compartment_id: str,
                  load_balancer_ocid: str,
                  post_path: str,
                  post_json,
                  method: str):
    url = f"{lb_api_endpoint}/{load_balancer_ocid}/{post_path}?compartmentId={compartment_id}"
    print(f"retryRestCall {url}")
    for i in range(1, 3):
        response = restCall(url, post_json, method)
        if response.status_code != 204:
            print(
                f"create {post_path} failed, retry in 15s, error body, {response.text}")
            time.sleep(15)
        else:
            break