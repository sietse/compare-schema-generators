from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_update_report_type import OadrUpdateReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdateReport(OadrUpdateReportType):
    """
    Send a previously requested report.
    """
    class Meta:
        name = "oadrUpdateReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
