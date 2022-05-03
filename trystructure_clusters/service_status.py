from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.espiservice_status_value import EspiserviceStatusValue
from trystructure_clusters.object_1 import Object1

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ServiceStatus(Object1):
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
