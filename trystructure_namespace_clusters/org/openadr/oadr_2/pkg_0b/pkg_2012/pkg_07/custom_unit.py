from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.base_unit_type import BaseUnitType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CustomUnit(BaseUnitType):
    class Meta:
        name = "customUnit"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
