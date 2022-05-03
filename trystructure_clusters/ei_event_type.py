from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.ei_active_period import EiActivePeriod
from trystructure_clusters.ei_event_signals import EiEventSignals
from trystructure_clusters.ei_target import EiTarget
from trystructure_clusters.event_descriptor import EventDescriptor

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventType:
    class Meta:
        name = "eiEventType"

    event_descriptor: Optional[EventDescriptor] = field(
        default=None,
        metadata={
            "name": "eventDescriptor",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    ei_active_period: Optional[EiActivePeriod] = field(
        default=None,
        metadata={
            "name": "eiActivePeriod",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    ei_event_signals: Optional[EiEventSignals] = field(
        default=None,
        metadata={
            "name": "eiEventSignals",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    ei_target: Optional[EiTarget] = field(
        default=None,
        metadata={
            "name": "eiTarget",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
