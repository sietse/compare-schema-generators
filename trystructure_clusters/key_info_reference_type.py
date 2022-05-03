from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class KeyInfoReferenceType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
