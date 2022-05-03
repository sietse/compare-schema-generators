from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.dsakey_value_type import DsakeyValueType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
