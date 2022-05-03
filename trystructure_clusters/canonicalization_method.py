from dataclasses import dataclass
from trystructure_clusters.canonicalization_method_type import CanonicalizationMethodType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
