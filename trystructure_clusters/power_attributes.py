from dataclasses import dataclass
from trystructure_clusters.power_attributes_type import PowerAttributesType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerAttributes(PowerAttributesType):
    class Meta:
        name = "powerAttributes"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
