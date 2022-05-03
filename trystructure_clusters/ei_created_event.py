from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.ei_response import EiResponse
from trystructure_clusters.event_responses import EventResponses

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"


@dataclass
class EiCreatedEvent:
    """
    Respond to a DR Event with optIn or optOut.
    """
    class Meta:
        name = "eiCreatedEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    event_responses: Optional[EventResponses] = field(
        default=None,
        metadata={
            "name": "eventResponses",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ven_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
