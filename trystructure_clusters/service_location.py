from dataclasses import dataclass
from trystructure_clusters.service_location_type import ServiceLocationType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceLocation(ServiceLocationType):
    class Meta:
        name = "serviceLocation"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
