from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signature_method_type import SignatureMethodType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
