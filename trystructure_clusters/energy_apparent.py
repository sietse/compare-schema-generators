from dataclasses import dataclass
from trystructure_clusters.energy_apparent_type import EnergyApparentType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyApparent(EnergyApparentType):
    class Meta:
        name = "energyApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
