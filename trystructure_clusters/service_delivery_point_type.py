from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceDeliveryPointType:
    """Logical point on the network where the ownership of the service changes
    hands.

    It is one of potentially many service points within a
    ServiceLocation, delivering service in accordance with a
    CustomerAgreement. Used at the place where a meter may be installed.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
