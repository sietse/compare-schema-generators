from dataclasses import dataclass
from trystructure_clusters.oadr_updated_report_type import OadrUpdatedReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdatedReport(OadrUpdatedReportType):
    """
    Acknowledge receipt of a report.
    """
    class Meta:
        name = "oadrUpdatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
