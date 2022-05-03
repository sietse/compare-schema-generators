from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_payload_resource_status import OadrPayloadResourceStatus
from trystructure_clusters.payload_float import PayloadFloat
from trystructure_clusters.stream_payload_base_type import StreamPayloadBaseType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalPayloadType(StreamPayloadBaseType):
    class Meta:
        name = "signalPayloadType"

    oadr_payload_resource_status: Optional[OadrPayloadResourceStatus] = field(
        default=None,
        metadata={
            "name": "oadrPayloadResourceStatus",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
