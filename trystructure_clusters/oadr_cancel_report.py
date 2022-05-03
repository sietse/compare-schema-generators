from dataclasses import dataclass
from trystructure_clusters.oadr_cancel_report_type import OadrCancelReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelReport(OadrCancelReportType):
    """
    Cancel a report.
    """
    class Meta:
        name = "oadrCancelReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
