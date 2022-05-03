from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.payload_float import PayloadFloat

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class CurrentValueType:
    class Meta:
        name = "currentValueType"

    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
