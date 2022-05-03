from dataclasses import dataclass
from trystructure_clusters.eckey_value_type import EckeyValueType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class EckeyValue(EckeyValueType):
    class Meta:
        name = "ECKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"
