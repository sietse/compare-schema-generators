from dataclasses import dataclass
from trystructure_clusters.dsakey_value_type import DsakeyValueType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
