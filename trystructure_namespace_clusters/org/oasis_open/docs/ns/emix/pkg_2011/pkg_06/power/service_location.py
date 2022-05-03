from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.service_location_type import ServiceLocationType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceLocation(ServiceLocationType):
    class Meta:
        name = "serviceLocation"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
