from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.dtstart import Dtstart
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration import Duration
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.pkg_0.stream.intervals import Intervals

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0:stream"


@dataclass
class StreamBaseType:
    """
    abstract base for communication of schedules for signals and observations.
    """
    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
        }
    )
