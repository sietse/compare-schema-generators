from dataclasses import dataclass, field
from trystructure_clusters.energy_item_type import EnergyItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyApparentType(EnergyItemType):
    """
    Apparent Energy, measured in volt-ampere hours (VAh)
    """
    item_description: str = field(
        init=False,
        default="ApparentEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
