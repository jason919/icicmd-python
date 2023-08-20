from oci.config import from_file
from oci.signer import Signer

config = from_file()
auth = Signer(
    tenancy=config['tenancy'],
    user=config['user'],
    fingerprint=config['fingerprint'],
    private_key_file_location=config['key_file']
)
LbApiEndpoint = "https://iaas.us-ashburn-1.oraclecloud.com/20170115/loadBalancers"
