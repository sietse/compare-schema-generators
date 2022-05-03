from dataclasses import dataclass
from trystructure_clusters.power_real_type import PowerRealType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerReal(PowerRealType):
    class Meta:
        name = "powerReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
