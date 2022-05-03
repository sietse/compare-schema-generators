from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.dtstart import Dtstart
from trystructure_clusters.duration import Duration
from trystructure_clusters.oadr_gbpayload import OadrGbpayload
from trystructure_clusters.oadr_report_payload import OadrReportPayload
from trystructure_clusters.signal_payload import SignalPayload
from trystructure_clusters.uid import Uid

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class IntervalType:
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
    uid: Optional[Uid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    oadr_report_payload: List[OadrReportPayload] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportPayload",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_gbpayload: List[OadrGbpayload] = field(
        default_factory=list,
        metadata={
            "name": "oadrGBPayload",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    signal_payload: List[SignalPayload] = field(
        default_factory=list,
        metadata={
            "name": "signalPayload",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
