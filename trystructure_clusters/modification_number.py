from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ModificationNumber:
    """
    Incremented each time an event is modified.
    """
    class Meta:
        name = "modificationNumber"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
