import json

from config import orb_certs, octa_certs, self_prod_certs, self_dev_certs
from helper.oci_http_helper import OCIHttpHelper


class Cert:
    @staticmethod
    def fix_certs_in_creation_json(certs_json):
        for value in certs_json.values():
            Cert.__fix_certs_in_creation_json(value)

    @staticmethod
    def __fix_certs_in_creation_json(cert_json):
        json_str = json.dumps(cert_json)
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
            cert_json["caCertificate"] = self_dev_certs["ca"]
        elif "InternalSelfCert-Prod-CERT" in json_str:
            cert_json["publicCertificate"] = self_prod_certs["public"]
            cert_json["privateKey"] = self_prod_certs["private"]
            cert_json["caCertificate"] = self_prod_certs["ca"]

    @staticmethod
    def create(compartment_id, load_balancer_ocid, post_json):
        Cert.__fix_certs_in_creation_json(post_json)
        OCIHttpHelper.retryRestCall(compartment_id,
                                    load_balancer_ocid,
                                    "certificates",
                                    post_json,
                                    "POST")
