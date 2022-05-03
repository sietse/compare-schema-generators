from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class NumDataSources:
    class Meta:
        name = "numDataSources"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
