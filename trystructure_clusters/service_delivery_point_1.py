from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.object_1 import Object1

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ServiceDeliveryPoint1(Object1):
    """
    [extension] Service Delivery Point is representation of revenue UsagePoint
    attributes.

    :ivar name: The name is any free human readable and possibly non
        unique text naming the object.
    :ivar tariff_profile: A schedule of charges; structure associated
        with Tariff that allows the definition of complex tariff
        structures such as step and time of use.
    :ivar customer_agreement: Agreement between the customer and the
        ServiceSupplier to pay for service at a specific service
        location. It provides for the recording of certain billing
        information about the type of service provided at the service
        location and is used during charge creation to determine the
        type of service.
    """
    class Meta:
        name = "ServiceDeliveryPoint"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    tariff_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "tariffProfile",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    customer_agreement: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAgreement",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
