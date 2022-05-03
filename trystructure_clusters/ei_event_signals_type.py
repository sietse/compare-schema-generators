from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.ei_event_baseline import EiEventBaseline
from trystructure_clusters.ei_event_signal import EiEventSignal

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignalsType:
    """
    :ivar ei_event_signal: Interval data for an event
    :ivar ei_event_baseline: Interval data for a baseline
    """
    class Meta:
        name = "eiEventSignalsType"

    ei_event_signal: List[EiEventSignal] = field(
        default_factory=list,
        metadata={
            "name": "eiEventSignal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
    ei_event_baseline: Optional[EiEventBaseline] = field(
        default=None,
        metadata={
            "name": "eiEventBaseline",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
