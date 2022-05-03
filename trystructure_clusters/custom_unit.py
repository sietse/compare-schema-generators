from dataclasses import dataclass
from trystructure_clusters.base_unit_type import BaseUnitType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CustomUnit(BaseUnitType):
    class Meta:
        name = "customUnit"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
