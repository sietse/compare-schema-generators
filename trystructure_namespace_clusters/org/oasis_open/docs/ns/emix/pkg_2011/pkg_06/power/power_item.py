from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.power_item_type import PowerItemType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerItem(PowerItemType):
    class Meta:
        name = "powerItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
