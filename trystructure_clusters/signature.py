from dataclasses import dataclass
from trystructure_clusters.signature_type import SignatureType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
