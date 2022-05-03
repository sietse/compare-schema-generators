from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.derencoded_key_value_type import DerencodedKeyValueType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class DerencodedKeyValue(DerencodedKeyValueType):
    class Meta:
        name = "DEREncodedKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"
