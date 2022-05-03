from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.curve_type import CurveType
from trystructure_clusters.ecvalidation_data_type import EcvalidationDataType
from trystructure_clusters.field_idtype import FieldIdtype

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class EcparametersType:
    class Meta:
        name = "ECParametersType"

    field_id: Optional[FieldIdtype] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    curve: Optional[CurveType] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    base: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    order: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    co_factor: Optional[int] = field(
        default=None,
        metadata={
            "name": "CoFactor",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    validation_data: Optional[EcvalidationDataType] = field(
        default=None,
        metadata={
            "name": "ValidationData",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
