from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrLoadControlStateTypeType:
    class Meta:
        name = "oadrLoadControlStateTypeType"

    oadr_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrMin",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrMax",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrCurrent",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_normal: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrNormal",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
