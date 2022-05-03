from dataclasses import dataclass
from trystructure_clusters.power_item_type import PowerItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerItem(PowerItemType):
    class Meta:
        name = "powerItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
