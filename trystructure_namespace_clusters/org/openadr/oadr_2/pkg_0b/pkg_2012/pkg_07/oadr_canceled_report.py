from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_canceled_report_type import OadrCanceledReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledReport(OadrCanceledReportType):
    class Meta:
        name = "oadrCanceledReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
