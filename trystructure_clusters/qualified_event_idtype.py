from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class QualifiedEventIdtype:
    """
    Fully qualified event ID includes the eventID and the modificationNumber.
    """
    class Meta:
        name = "QualifiedEventIDType"

    event_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    modification_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "modificationNumber",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
