from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.energy_real_type import EnergyRealType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyReal(EnergyRealType):
    class Meta:
        name = "energyReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
