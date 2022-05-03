from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.oadr_info import OadrInfo
from trystructure_clusters.oadr_service_name_type import OadrServiceNameType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrServiceSpecificInfo:
    """
    Service specific registration information.
    """
    class Meta:
        name = "oadrServiceSpecificInfo"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_service: List["OadrServiceSpecificInfo.OadrService"] = field(
        default_factory=list,
        metadata={
            "name": "oadrService",
            "type": "Element",
        }
    )

    @dataclass
    class OadrService:
        oadr_service_name: Optional[OadrServiceNameType] = field(
            default=None,
            metadata={
                "name": "oadrServiceName",
                "type": "Element",
                "required": True,
            }
        )
        oadr_info: List[OadrInfo] = field(
            default_factory=list,
            metadata={
                "name": "oadrInfo",
                "type": "Element",
                "min_occurs": 1,
            }
        )
