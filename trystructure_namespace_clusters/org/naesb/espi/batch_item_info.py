from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.crudoperation_value import CrudoperationValue
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object
from trystructure_namespace_clusters.org.naesb.espi.status_code_value import StatusCodeValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class BatchItemInfo(Object):
    """
    Includes elements that make it possible to include multiple transactions in
    a single (batch) request.

    :ivar name: An identifier for this object that is only unique within
        the containing collection.
    :ivar operation: Specifies the operation requested of this item.
    :ivar status_code: Indicates the status code of the associated
        transaction.
    :ivar status_reason: Indicates the reason for the indicated status
        code.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    name: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    operation: Optional[Union[int, CrudoperationValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    status_code: Optional[Union[int, StatusCodeValue]] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
        }
    )
    status_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusReason",
            "type": "Element",
            "max_length": 256,
        }
    )
