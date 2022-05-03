from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_filenames.oadr_ei_20b import Interval
from trystructure_filenames.oadr_xcal_20b import (
    Dtstart,
    Duration,
)

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0:stream"


@dataclass
class StreamPayloadBaseType:
    """Abstract class to convey a payload for a stream.

    When a Stream is transformed to or from a WS-Calendar Interval, the
    contents of the Stream Payload defined element are transformed into
    the contents of a WS-Calendar artifactBase.
    """


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
