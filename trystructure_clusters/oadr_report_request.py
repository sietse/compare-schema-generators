from dataclasses import dataclass
from trystructure_clusters.oadr_report_request_type import OadrReportRequestType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportRequest(OadrReportRequestType):
    class Meta:
        name = "oadrReportRequest"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
