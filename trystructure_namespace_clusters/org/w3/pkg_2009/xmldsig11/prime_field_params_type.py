from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PrimeFieldParamsType:
    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
