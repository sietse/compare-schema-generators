from dataclasses import dataclass
from trystructure_clusters.voltage_type import VoltageType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Voltage(VoltageType):
    class Meta:
        name = "voltage"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
