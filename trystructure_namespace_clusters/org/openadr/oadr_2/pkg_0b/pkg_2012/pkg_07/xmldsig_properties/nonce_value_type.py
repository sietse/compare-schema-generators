from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


@dataclass
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
