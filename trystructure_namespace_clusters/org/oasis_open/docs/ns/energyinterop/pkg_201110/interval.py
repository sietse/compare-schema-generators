from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.interval_type import IntervalType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Interval(IntervalType):
    class Meta:
        name = "interval"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
