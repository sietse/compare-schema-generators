from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.date_time_interval import DateTimeInterval
from trystructure_clusters.object_1 import Object1
from trystructure_clusters.reading_quality import ReadingQuality

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class IntervalReading(Object1):
    """Specific value measured by a meter or other asset.

    Each Reading is associated with a specific ReadingType.

    :ivar cost: [correction] Specifies a cost associated with this
        reading, in hundred-thousandths of the currency specified in the
        ReadingType for this reading. (e.g., 840 = USD, US dollar)
    :ivar reading_quality:
    :ivar time_period: The date time and duration of a reading. If not
        specified, readings for each "intervalLength" in ReadingType are
        present.
    :ivar value: [correction] Value in units specified by ReadingType
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    cost: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    reading_quality: List[ReadingQuality] = field(
        default_factory=list,
        metadata={
            "name": "ReadingQuality",
            "type": "Element",
        }
    )
    time_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timePeriod",
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
