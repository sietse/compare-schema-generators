from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.batch_item_info import BatchItemInfo
from trystructure_clusters.object_1 import Object1

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class IdentifiedObject(Object1):
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
