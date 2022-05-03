from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.pulse_count_type import PulseCountType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class PulseCount(PulseCountType):
    class Meta:
        name = "pulseCount"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
