from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.dtstart import Dtstart
from trystructure_clusters.duration import Duration
from trystructure_clusters.intervals import Intervals

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
