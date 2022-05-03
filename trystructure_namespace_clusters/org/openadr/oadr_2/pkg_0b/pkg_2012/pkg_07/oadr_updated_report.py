from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_updated_report_type import OadrUpdatedReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdatedReport(OadrUpdatedReportType):
    """
    Acknowledge receipt of a report.
    """
    class Meta:
        name = "oadrUpdatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
