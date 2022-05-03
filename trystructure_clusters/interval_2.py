from dataclasses import dataclass
from trystructure_clusters.interval_type import IntervalType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Interval2(IntervalType):
    class Meta:
        name = "interval"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
