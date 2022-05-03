from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class TransportInterfaceType:
    """
    The Transport Interface delineates the edges at either end of a transport
    segment.
    """
    point_of_receipt: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfReceipt",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    point_of_delivery: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfDelivery",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
