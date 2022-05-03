from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


@dataclass(unsafe_hash=True, frozen=True)
class NonceValueType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    encoding_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "EncodingType",
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ReplayProtectType:
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )
    nonce: Optional[NonceValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ReplayProtect(ReplayProtectType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"
