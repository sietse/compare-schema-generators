from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.pkg_0.stream.stream_payload_base_type import StreamPayloadBaseType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.payload_float import PayloadFloat
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_payload_resource_status import OadrPayloadResourceStatus

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportPayloadType(StreamPayloadBaseType):
    """
    Report Payload for use in Reports, snaps, and projections.

    :ivar r_id: A reference to a metadata data point description
    :ivar confidence: Likely variability of prediction: 0-100
    :ivar accuracy: Accuracy in same units as interval payload value
    :ivar oadr_payload_resource_status:
    :ivar payload_float:
    """
    r_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "rID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    confidence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
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
