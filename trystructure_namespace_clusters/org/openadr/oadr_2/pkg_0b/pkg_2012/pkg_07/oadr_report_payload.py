from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_report_payload_type import OadrReportPayloadType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportPayload(OadrReportPayloadType):
    """
    Data point values for reports.
    """
    class Meta:
        name = "oadrReportPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
