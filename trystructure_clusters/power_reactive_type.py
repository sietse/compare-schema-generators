from dataclasses import dataclass, field
from trystructure_clusters.power_item_type import PowerItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerReactiveType(PowerItemType):
    """
    Reactive power, measured in volt-amperes reactive (VAR)
    """
    item_description: str = field(
        init=False,
        default="ReactivePower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAR",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
