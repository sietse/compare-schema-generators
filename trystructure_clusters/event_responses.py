from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.opt_type_type import OptTypeType
from trystructure_clusters.qualified_event_id import QualifiedEventId

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventResponses:
    """
    optIn or optOut responses for received events.
    """
    class Meta:
        name = "eventResponses"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    event_response: List["EventResponses.EventResponse"] = field(
        default_factory=list,
        metadata={
            "name": "eventResponse",
            "type": "Element",
        }
    )

    @dataclass
    class EventResponse:
        response_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "responseCode",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9][0-9][0-9]",
            }
        )
        response_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "responseDescription",
                "type": "Element",
            }
        )
        request_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "requestID",
                "type": "Element",
                "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
                "required": True,
            }
        )
        qualified_event_id: Optional[QualifiedEventId] = field(
            default=None,
            metadata={
                "name": "qualifiedEventID",
                "type": "Element",
                "required": True,
            }
        )
        opt_type: Optional[OptTypeType] = field(
            default=None,
            metadata={
                "name": "optType",
                "type": "Element",
                "required": True,
            }
        )
