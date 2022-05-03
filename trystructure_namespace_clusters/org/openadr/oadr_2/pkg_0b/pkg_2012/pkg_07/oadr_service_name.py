from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_service_name_type import OadrServiceNameType

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
