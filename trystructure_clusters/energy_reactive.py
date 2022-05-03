from dataclasses import dataclass
from trystructure_clusters.energy_reactive_type import EnergyReactiveType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyReactive(EnergyReactiveType):
    class Meta:
        name = "energyReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
