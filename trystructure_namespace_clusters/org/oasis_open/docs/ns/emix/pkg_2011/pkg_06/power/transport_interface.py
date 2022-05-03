from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.transport_interface_type import TransportInterfaceType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class TransportInterface(TransportInterfaceType):
    class Meta:
        name = "transportInterface"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
