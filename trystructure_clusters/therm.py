from dataclasses import dataclass
from trystructure_clusters.therm_type import ThermType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Therm(ThermType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
