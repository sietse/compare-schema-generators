from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.pkg_0.stream.stream_payload_base_type import StreamPayloadBaseType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.payload_float import PayloadFloat
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_payload_resource_status import OadrPayloadResourceStatus

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
