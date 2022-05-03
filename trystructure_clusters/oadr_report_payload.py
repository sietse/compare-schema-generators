from dataclasses import dataclass
from trystructure_clusters.oadr_report_payload_type import OadrReportPayloadType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportPayload(OadrReportPayloadType):
    """
    Data point values for reports.
    """
    class Meta:
        name = "oadrReportPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
