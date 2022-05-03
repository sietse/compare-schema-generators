from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class EcvalidationDataType:
    class Meta:
        name = "ECValidationDataType"

    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    hash_algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "hashAlgorithm",
            "type": "Attribute",
            "required": True,
        }
    )
