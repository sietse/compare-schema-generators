from dataclasses import dataclass
from trystructure_clusters.power_reactive_type import PowerReactiveType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerReactive(PowerReactiveType):
    class Meta:
        name = "powerReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
