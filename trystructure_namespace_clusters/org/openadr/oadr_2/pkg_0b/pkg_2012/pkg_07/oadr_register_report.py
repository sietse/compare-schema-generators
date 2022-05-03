from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_register_report_type import OadrRegisterReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRegisterReport(OadrRegisterReportType):
    """
    Register Metadata report settings with other party.
    """
    class Meta:
        name = "oadrRegisterReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
