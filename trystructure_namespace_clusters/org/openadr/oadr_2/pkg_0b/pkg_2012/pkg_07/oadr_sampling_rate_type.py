from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrSamplingRateType:
    """
    :ivar oadr_min_period: Minimum sampling period
    :ivar oadr_max_period: Maximum sampling period
    :ivar oadr_on_change: If true then the data will be recorded when it
        changes, but at no greater a frequency than that specified  by
        minPeriod.
    """
    class Meta:
        name = "oadrSamplingRateType"

    oadr_min_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrMinPeriod",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )
    oadr_max_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrMaxPeriod",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )
    oadr_on_change: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrOnChange",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
