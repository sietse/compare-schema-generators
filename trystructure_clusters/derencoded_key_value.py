from dataclasses import dataclass
from trystructure_clusters.derencoded_key_value_type import DerencodedKeyValueType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class DerencodedKeyValue(DerencodedKeyValueType):
    class Meta:
        name = "DEREncodedKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"
