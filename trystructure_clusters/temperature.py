from dataclasses import dataclass
from trystructure_clusters.temperature_type import TemperatureType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Temperature(TemperatureType):
    class Meta:
        name = "temperature"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
