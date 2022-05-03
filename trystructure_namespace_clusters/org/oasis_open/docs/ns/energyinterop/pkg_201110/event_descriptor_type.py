from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.event_status_enumerated_type import EventStatusEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventDescriptorType:
    """
    :ivar event_id:
    :ivar modification_number:
    :ivar modification_date_time: When an event is modified
    :ivar modification_reason: Why an event was modified
    :ivar priority: The priority of the event in relation to other
        events (The lower the number higher the priority. A value of
        zero (0) indicates no priority, which is the lowest priority by
        default).
    :ivar ei_market_context:
    :ivar created_date_time:
    :ivar event_status: An indication of the event state: far, near,
        active, canceled, completed
    :ivar test_event: Anything other than false indicates a test event
    :ivar vtn_comment: Any text
    """
    class Meta:
        name = "eventDescriptorType"

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
    modification_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "modificationDateTime",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
    modification_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "modificationReason",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ei_market_context: Optional["EventDescriptorType.EiMarketContext"] = field(
        default=None,
        metadata={
            "name": "eiMarketContext",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
    event_status: Optional[EventStatusEnumeratedType] = field(
        default=None,
        metadata={
            "name": "eventStatus",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    test_event: Optional[str] = field(
        default=None,
        metadata={
            "name": "testEvent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    vtn_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtnComment",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )

    @dataclass
    class EiMarketContext:
        market_context: Optional[str] = field(
            default=None,
            metadata={
                "name": "marketContext",
                "type": "Element",
                "namespace": "http://docs.oasis-open.org/ns/emix/2011/06",
                "required": True,
            }
        )
