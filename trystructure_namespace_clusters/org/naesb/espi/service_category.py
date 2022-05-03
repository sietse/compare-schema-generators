from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object
from trystructure_namespace_clusters.org.naesb.espi.service_kind_value import ServiceKindValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ServiceCategory(Object):
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
