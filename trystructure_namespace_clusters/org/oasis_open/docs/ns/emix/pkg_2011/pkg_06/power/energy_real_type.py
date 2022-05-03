from dataclasses import dataclass, field
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.energy_item_type import EnergyItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyRealType(EnergyItemType):
    """
    Real Energy, Watt Hours (Wh)
    """
    item_description: str = field(
        init=False,
        default="RealEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="Wh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
