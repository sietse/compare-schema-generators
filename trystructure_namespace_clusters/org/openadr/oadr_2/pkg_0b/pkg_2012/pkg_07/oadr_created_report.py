from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_created_report_type import OadrCreatedReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedReport(OadrCreatedReportType):
    """
    Acknowledge the request for report was received.
    """
    class Meta:
        name = "oadrCreatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
