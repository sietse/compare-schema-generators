from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.rsakey_value_type import RsakeyValueType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
