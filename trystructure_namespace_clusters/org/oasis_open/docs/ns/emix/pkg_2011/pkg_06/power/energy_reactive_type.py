from dataclasses import dataclass, field
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.energy_item_type import EnergyItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyReactiveType(EnergyItemType):
    """
    Reactive Energy, volt-amperes reactive hours (VARh)
    """
    item_description: str = field(
        init=False,
        default="ReactiveEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VARh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
