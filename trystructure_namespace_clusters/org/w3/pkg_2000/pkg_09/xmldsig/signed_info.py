from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signed_info_type import SignedInfoType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignedInfo(SignedInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
