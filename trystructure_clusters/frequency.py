from dataclasses import dataclass
from trystructure_clusters.frequency_type import FrequencyType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Frequency(FrequencyType):
    class Meta:
        name = "frequency"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
