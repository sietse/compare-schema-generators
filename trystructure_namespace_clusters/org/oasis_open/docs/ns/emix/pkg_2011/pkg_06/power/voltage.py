from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.voltage_type import VoltageType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Voltage(VoltageType):
    class Meta:
        name = "voltage"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
