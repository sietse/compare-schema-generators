from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.object_1 import Object1

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class DateTimeInterval(Object1):
    """Interval of date and time.

    End is not included because it can be derived from the start and the
    duration.

    :ivar duration: [correction] Duration of the interval, in seconds.
    :ivar start: [correction] Date and time that this interval started.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
