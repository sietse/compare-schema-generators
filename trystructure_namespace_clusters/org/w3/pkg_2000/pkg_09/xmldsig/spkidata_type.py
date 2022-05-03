from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SpkidataType:
    class Meta:
        name = "SPKIDataType"

    spkisexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SPKISexp",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "sequential": True,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )
