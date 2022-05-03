from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Confidence:
    class Meta:
        name = "confidence"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )
