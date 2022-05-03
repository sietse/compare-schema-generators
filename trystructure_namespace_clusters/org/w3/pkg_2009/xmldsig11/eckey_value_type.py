from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.ecparameters_type import EcparametersType
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.named_curve_type import NamedCurveType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class EckeyValueType:
    class Meta:
        name = "ECKeyValueType"

    ecparameters: Optional[EcparametersType] = field(
        default=None,
        metadata={
            "name": "ECParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    named_curve: Optional[NamedCurveType] = field(
        default=None,
        metadata={
            "name": "NamedCurve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    public_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PublicKey",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
