from dataclasses import dataclass
from trystructure_clusters.power_apparent_type import PowerApparentType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerApparent(PowerApparentType):
    class Meta:
        name = "powerApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
