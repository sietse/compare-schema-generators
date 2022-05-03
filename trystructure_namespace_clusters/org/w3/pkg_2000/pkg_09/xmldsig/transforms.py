from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.transforms_type import TransformsType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transforms(TransformsType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
