from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.identified_object import IdentifiedObject

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class TimeConfiguration(IdentifiedObject):
    """
    [extension] Contains attributes related to the configuration of the time
    service.

    :ivar dst_end_rule: Rule to calculate end of daylight savings time
        in the current year.  Result of dstEndRule must be greater than
        result of dstStartRule.
    :ivar dst_offset: Daylight savings time offset from local standard
        time.
    :ivar dst_start_rule: Rule to calculate start of daylight savings
        time in the current year. Result of dstEndRule must be greater
        than result of dstStartRule.
    :ivar tz_offset: Local time zone offset from UTCTime. Does not
        include any daylight savings time offsets.
    """
    dst_end_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstEndRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    dst_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "dstOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    dst_start_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstStartRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    tz_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "tzOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
