from dataclasses import dataclass, field
from trystructure_clusters.power_item_type import PowerItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerRealType(PowerItemType):
    """
    Real power measured in Watts (W) or Joules/second (J/s)
    """
    item_description: str = field(
        init=False,
        default="RealPower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
