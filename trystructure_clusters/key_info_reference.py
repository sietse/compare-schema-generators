from dataclasses import dataclass
from trystructure_clusters.key_info_reference_type import KeyInfoReferenceType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class KeyInfoReference(KeyInfoReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
