from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.power_apparent_type import PowerApparentType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerApparent(PowerApparentType):
    class Meta:
        name = "powerApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
