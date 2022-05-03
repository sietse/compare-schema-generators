from dataclasses import dataclass, field
from typing import List
from trystructure_clusters.interval_2 import Interval2

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0:stream"


@dataclass
class Intervals:
    """
    Time intervals during which the DR event is active or report data is
    available.
    """
    class Meta:
        name = "intervals"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0:stream"

    interval: List[Interval2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
