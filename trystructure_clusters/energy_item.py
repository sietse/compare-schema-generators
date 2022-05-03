from dataclasses import dataclass
from trystructure_clusters.energy_item_type import EnergyItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyItem(EnergyItemType):
    class Meta:
        name = "energyItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
