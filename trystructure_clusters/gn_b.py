from dataclasses import dataclass
from trystructure_clusters.char_two_field_params_type import CharTwoFieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class GnB(CharTwoFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
