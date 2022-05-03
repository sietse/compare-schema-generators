from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.object_1 import Object1
from trystructure_clusters.service_kind_value import ServiceKindValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ServiceCategory(Object1):
    """
    Category of service provided to the customer.

    :ivar kind: Service classification Examples are: 0 - electricity 1 -
        gas The list of specific valid values per the standard are
        itemized in ServiceKind.
    """
    kind: Optional[Union[int, ServiceKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
