from dataclasses import dataclass
from trystructure_clusters.oadr_create_report_type import OadrCreateReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreateReport(OadrCreateReportType):
    """
    Request report from other party.
    """
    class Meta:
        name = "oadrCreateReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
