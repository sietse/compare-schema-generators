from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.report_payload_type import ReportPayloadType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_data_quality_type import OadrDataQualityType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportPayloadType(ReportPayloadType):
    """
    Report payload for use in reports.

    :ivar oadr_data_quality: Enumerated value for the quality of this
        data item
    """
    class Meta:
        name = "oadrReportPayloadType"

    oadr_data_quality: Optional[Union[OadrDataQualityType, str]] = field(
        default=None,
        metadata={
            "name": "oadrDataQuality",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "pattern": r"x-\S.*",
        }
    )
