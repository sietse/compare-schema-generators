from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.espiservice_status_value import EspiserviceStatusValue
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ServiceStatus(Object):
    """
    Contains the current status of the service.

    :ivar current_status: The current status of the service.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    current_status: Optional[Union[int, EspiserviceStatusValue]] = field(
        default=None,
        metadata={
            "name": "currentStatus",
            "type": "Element",
            "required": True,
        }
    )
