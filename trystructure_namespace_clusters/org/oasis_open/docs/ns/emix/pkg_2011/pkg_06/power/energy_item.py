from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.energy_item_type import EnergyItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyItem(EnergyItemType):
    class Meta:
        name = "energyItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
