from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.report_specifier import ReportSpecifier

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportRequestType:
    """
    This type is used to request an EiReport.
    """
    class Meta:
        name = "oadrReportRequestType"

    report_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_specifier: Optional[ReportSpecifier] = field(
        default=None,
        metadata={
            "name": "reportSpecifier",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
