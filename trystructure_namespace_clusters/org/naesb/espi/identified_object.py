from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.naesb.espi.batch_item_info import BatchItemInfo
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class IdentifiedObject(Object):
    """
    This is a root class to provide common naming attributes for all classes
    needing naming attributes.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    batch_item_info: Optional[BatchItemInfo] = field(
        default=None,
        metadata={
            "name": "batchItemInfo",
            "type": "Element",
        }
    )
