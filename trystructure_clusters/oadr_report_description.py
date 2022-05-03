from dataclasses import dataclass
from trystructure_clusters.oadr_report_description_type import OadrReportDescriptionType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportDescription(OadrReportDescriptionType):
    class Meta:
        name = "oadrReportDescription"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
