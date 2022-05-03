from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.char_two_field_params_type import CharTwoFieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "TnBFieldParamsType"

    k: Optional[int] = field(
        default=None,
        metadata={
            "name": "K",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
