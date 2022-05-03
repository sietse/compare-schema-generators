from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.dtstart import Dtstart
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration import Duration
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.uid import Uid
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.signal_payload import SignalPayload
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_gbpayload import OadrGbpayload
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_report_payload import OadrReportPayload

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
