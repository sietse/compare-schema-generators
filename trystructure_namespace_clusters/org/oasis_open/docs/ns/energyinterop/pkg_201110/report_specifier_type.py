from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration_prop_type import DurationPropType
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.granularity import Granularity
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.ws_calendar_interval_type import WsCalendarIntervalType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.specifier_payload import SpecifierPayload

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportSpecifierType:
    """
    Parameters that define the content of a Report Stream.

    :ivar report_specifier_id:
    :ivar granularity: How frequently the [measurement] is to be
        recorded.
    :ivar report_back_duration: Report back with the Report-To-Date for
        each passing of this Duration.
    :ivar report_interval: This is the overall period of reporting.
    :ivar specifier_payload:
    """
    report_specifier_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportSpecifierID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    granularity: Optional[Granularity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    report_back_duration: Optional[DurationPropType] = field(
        default=None,
        metadata={
            "name": "reportBackDuration",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_interval: Optional[WsCalendarIntervalType] = field(
        default=None,
        metadata={
            "name": "reportInterval",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    specifier_payload: List[SpecifierPayload] = field(
        default_factory=list,
        metadata={
            "name": "specifierPayload",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
