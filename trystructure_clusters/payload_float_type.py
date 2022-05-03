from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.payload_base_type import PayloadBaseType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class PayloadFloatType(PayloadBaseType):
    """
    This is the payload for signals that require a quantity.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
