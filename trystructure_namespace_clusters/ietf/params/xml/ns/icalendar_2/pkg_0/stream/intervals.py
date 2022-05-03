from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.interval import Interval

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

    interval: List[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
