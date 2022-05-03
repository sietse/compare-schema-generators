from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.naesb.espi.identified_object import IdentifiedObject
from trystructure_namespace_clusters.org.naesb.espi.service_category import ServiceCategory
from trystructure_namespace_clusters.org.naesb.espi.service_delivery_point import ServiceDeliveryPoint

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class UsagePoint(IdentifiedObject):
    """
    Logical point on a network at which consumption or production is either
    physically measured (e.g., metered) or estimated (e.g., unmetered street
    lights).

    :ivar role_flags: Specifies the roles that this usage point has been
        assigned. Bit 1 - isMirror Bit 2 - isPremisesAggregationPoint
        Bit 3 - isPEV Bit 4 - isDER Bit 5 - isRevenueQuality Bit 6 -
        isDC Bit 7-16 - Reserved
    :ivar service_category:
    :ivar status: Specifies the current status of this usage point.
        Valid values include: 0 = off 1 = on
    :ivar service_delivery_point: [extension] Contains service delivery
        point information about the UsagePoint if it does represent the
        service delivery point.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    role_flags: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "roleFlags",
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    service_delivery_point: Optional[ServiceDeliveryPoint] = field(
        default=None,
        metadata={
            "name": "ServiceDeliveryPoint",
            "type": "Element",
        }
    )
