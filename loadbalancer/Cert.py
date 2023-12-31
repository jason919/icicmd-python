import json
import os
import time

from config import orb_certs, octa_certs, self_prod_certs, self_dev_certs
from helper import OciHttpHelper, JsonHelper
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
    elif "myaccount.405expresslanes.com" in json_str:
        cert_json["publicCertificate"] = octa_certs["public-405"]
        cert_json["privateKey"] = octa_certs["private-405"]
        cert_json["caCertificate"] = octa_certs["ca-405"]


def update_expired_cert_for_compartment(
    new_cert_folder_path: str, json_file_name: str, cert_name: str
):
    with open(
        f"{os.getcwd()}/resources/files/saved/{json_file_name}", "r"
    ) as json_file:
        json_text = json_file.read()
    lb_names = JsonHelper.get_lb_names_from_compartment_json(json_text)
    for lb_name in lb_names:
        update_expired_cert(new_cert_folder_path, json_file_name, cert_name, lb_name)


def update_expired_cert(
    new_cert_folder_path: str,
    json_file_name: str,
    cert_name: str,
    load_balancer_name: str,
):
    tmp_cert_name = f"tmptmp-{cert_name}"

    with open(
        f"{os.getcwd()}/resources/files/saved/{json_file_name}", "r"
    ) as json_file:
        json_text = json_file.read()
    parsed_data = JsonHelper.get_lb_data_from_compartment_json(
        json_text, load_balancer_name
    )
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
    if "LB" in cert_name or "Wild" in cert_name:
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
    if "LB" in cert_name or "Wild" in cert_name:
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
