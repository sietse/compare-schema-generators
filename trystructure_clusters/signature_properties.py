from dataclasses import dataclass
from trystructure_clusters.signature_properties_type import SignaturePropertiesType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureProperties(SignaturePropertiesType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
