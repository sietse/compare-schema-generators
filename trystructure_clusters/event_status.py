from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.event_status_enumerated_type import EventStatusEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventStatus:
    class Meta:
        name = "eventStatus"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[EventStatusEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
