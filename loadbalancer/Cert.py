import json
import time

from config import orb_certs, octa_certs, self_prod_certs, self_dev_certs
from helper import OciHttpHelper
from loadbalancer import Backendset, Listener


def fix_certs_in_creation_json(certs_json):
    json_str: str = json.dumps(certs_json)
    if "LB-ORB-CERT" in json_str:
        client = "ORB"
    elif "LB-OCTA-CERT" in json_str:
        client = "OCTA"
    for value in certs_json.values():
        __fix_certs_in_creation_json(value, client)


def __fix_certs_in_creation_json(cert_json, client: str):
    json_str: str = json.dumps(cert_json)
    if "LB-ORB-CERT" in json_str:
        cert_json["publicCertificate"] = orb_certs["public"]
        cert_json["privateKey"] = orb_certs["private"]
        cert_json["caCertificate"] = orb_certs["ca"]
    elif "LB-OCTA-CERT" in json_str:
        cert_json["publicCertificate"] = octa_certs["public"]
        cert_json["privateKey"] = octa_certs["private"]
        cert_json["caCertificate"] = octa_certs["ca"]
    elif "InternalSelfCert-Dev-CERT" in json_str:
        cert_json["publicCertificate"] = self_dev_certs["public"]
        cert_json["privateKey"] = self_dev_certs["private"]
        cert_json["caCertificate"] = self_dev_certs["public"]
    elif "InternalSelfCert-Prod-CERT" in json_str:
        if "ORB" == client:
            cert_json["publicCertificate"] = self_prod_certs["orb-public"]
            cert_json["privateKey"] = self_prod_certs["orb-private"]
            cert_json["caCertificate"] = self_prod_certs["orb-public"]
        elif "OCTA" == client:
            print("replacing octa internal certs")
            cert_json["publicCertificate"] = self_prod_certs["octa-public"]
            cert_json["privateKey"] = self_prod_certs["octa-private"]
            cert_json["caCertificate"] = self_prod_certs["octa-public"]


def update_expired_cert(
    new_cert_folder_path: str,
    full_json_path: str,
    cert_name: str,
):
    tmp_cert_name = f"tmp-{cert_name}"

    with open(f"{full_json_path}", "r") as json_file:
        json_data = json_file.read()
    parsed_data = json.loads(json_data)
    compartment_id = str(parsed_data["compartmentId"])
    load_balancer_ocid = str(parsed_data["id"])

    post_json = {
        "privateKey": "",
        "publicCertificate": "",
        "caCertificate": "",
        "certificateName": tmp_cert_name,
    }
    with open(f"{new_cert_folder_path}/ca.crt", "r") as ca_file:
        post_json["caCertificate"] = ca_file.read()
    with open(f"{new_cert_folder_path}/private.pem", "r") as pri_file:
        post_json["privateKey"] = pri_file.read()
    with open(f"{new_cert_folder_path}/public.pem", "r") as pub_file:
        post_json["publicCertificate"] = pub_file.read()

    # create the tmp name certificate
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "certificates", post_json, "POST"
    )
    time.sleep(15)
    # set the certificate to the tmp name one
    if "LB-" in cert_name:
        Listener.update_listeners_with_cert_name(
            compartment_id, load_balancer_ocid, parsed_data, tmp_cert_name
        )
    else:
        Backendset.update_backend_sets_with_cert_name(
            compartment_id, load_balancer_ocid, parsed_data, tmp_cert_name
        )
    time.sleep(30)
    # delete the good name but expired certificate

    OciHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"certificates/{cert_name}",
        post_json,
        "DELETE",
    )

    time.sleep(15)
    post_json["certificateName"] = cert_name
    # create the good name and new certificate
    OciHttpHelper.retryRestCall(
        compartment_id, load_balancer_ocid, "certificates", post_json, "POST"
    )
    time.sleep(15)
    # set the certificate to the good name
    if "LB-" in cert_name:
        Listener.update_listeners_with_cert_name(
            compartment_id, load_balancer_ocid, parsed_data, cert_name
        )
    else:
        Backendset.update_backend_sets_with_cert_name(
            compartment_id, load_balancer_ocid, parsed_data, cert_name
        )
    time.sleep(30)
    # delete the tmp certificate
    OciHttpHelper.retryRestCall(
        compartment_id,
        load_balancer_ocid,
        f"certificates/{tmp_cert_name}",
        post_json,
        "DELETE",
    )
