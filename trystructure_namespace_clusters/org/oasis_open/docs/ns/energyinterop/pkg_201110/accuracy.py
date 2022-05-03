from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Accuracy:
    class Meta:
        name = "accuracy"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
