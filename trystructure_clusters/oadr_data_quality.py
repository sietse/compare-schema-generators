from dataclasses import dataclass, field
from typing import Union
from trystructure_clusters.oadr_data_quality_type import OadrDataQualityType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDataQuality:
    class Meta:
        name = "oadrDataQuality"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Union[OadrDataQualityType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
