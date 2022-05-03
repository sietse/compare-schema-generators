from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_load_control_state_type_type import OadrLoadControlStateTypeType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrLoadControlStateType:
    class Meta:
        name = "oadrLoadControlStateType"

    oadr_capacity: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrCapacity",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_level_offset: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrLevelOffset",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_percent_offset: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrPercentOffset",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_set_point: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrSetPoint",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
