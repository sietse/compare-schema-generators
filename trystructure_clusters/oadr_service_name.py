from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_service_name_type import OadrServiceNameType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrServiceName:
    class Meta:
        name = "oadrServiceName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrServiceNameType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
