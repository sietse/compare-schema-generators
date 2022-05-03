from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.naesb.espi.date_time_interval import DateTimeInterval
from trystructure_namespace_clusters.org.naesb.espi.identified_object import IdentifiedObject
from trystructure_namespace_clusters.org.naesb.espi.interval_reading import IntervalReading

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class IntervalBlock(IdentifiedObject):
    """
    Time sequence of Readings of the same ReadingType.

    :ivar interval: Specifies the time period during which the contained
        readings were taken.
    :ivar interval_reading:
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    interval_reading: List[IntervalReading] = field(
        default_factory=list,
        metadata={
            "name": "IntervalReading",
            "type": "Element",
        }
    )
