from dataclasses import dataclass
from trystructure_clusters.service_area_type import ServiceAreaType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06"


@dataclass
class ServiceArea(ServiceAreaType):
    class Meta:
        name = "serviceArea"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"
