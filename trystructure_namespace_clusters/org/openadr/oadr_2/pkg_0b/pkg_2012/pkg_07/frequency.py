from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.frequency_type import FrequencyType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Frequency(FrequencyType):
    class Meta:
        name = "frequency"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
