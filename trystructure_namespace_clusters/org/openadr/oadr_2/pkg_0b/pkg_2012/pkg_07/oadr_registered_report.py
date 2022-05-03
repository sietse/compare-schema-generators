from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_registered_report_type import OadrRegisteredReportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRegisteredReport(OadrRegisteredReportType):
    """
    Acknowledge registration of Metadata report by other party.
    """
    class Meta:
        name = "oadrRegisteredReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
