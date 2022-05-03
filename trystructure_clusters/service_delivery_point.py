from dataclasses import dataclass
from trystructure_clusters.service_delivery_point_type import ServiceDeliveryPointType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceDeliveryPoint(ServiceDeliveryPointType):
    class Meta:
        name = "serviceDeliveryPoint"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
