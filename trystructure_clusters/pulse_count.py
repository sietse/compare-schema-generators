from dataclasses import dataclass
from trystructure_clusters.pulse_count_type import PulseCountType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class PulseCount(PulseCountType):
    class Meta:
        name = "pulseCount"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
