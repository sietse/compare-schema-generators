from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.pkg_0.stream.stream_base_type import StreamBaseType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.report_name_enumerated_type import ReportNameEnumeratedType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_report_description import OadrReportDescription

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportType(StreamBaseType):
    """eiReport is a Stream of [measurements] recorded over time and delivered
    to the requestor periodically.

    The readings may be actual, computed, summed if derived in some
    other manner.

    :ivar ei_report_id: reference ID to this report.
    :ivar oadr_report_description: Define data points the implementation
        is capable of reporting on. Only used in Metadata report
    :ivar report_request_id: Reference to the oadrCreateReport request
        that defined this report.
    :ivar report_specifier_id: Reference to Metadata report from which
        this report was derived.
    :ivar report_name: Name possibly for use in a user interface.
    :ivar created_date_time:
    """
    class Meta:
        name = "oadrReportType"

    ei_report_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "eiReportID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    oadr_report_description: List[OadrReportDescription] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    report_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_specifier_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportSpecifierID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_name: Optional[Union[ReportNameEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "reportName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"x-\S.*",
        }
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
