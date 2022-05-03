from dataclasses import dataclass
from trystructure_clusters.oadr_report_type import OadrReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReport(OadrReportType):
    class Meta:
        name = "oadrReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
