from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.char_two_field_params_type import CharTwoFieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "PnBFieldParamsType"

    k1: Optional[int] = field(
        default=None,
        metadata={
            "name": "K1",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k2: Optional[int] = field(
        default=None,
        metadata={
            "name": "K2",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k3: Optional[int] = field(
        default=None,
        metadata={
            "name": "K3",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
