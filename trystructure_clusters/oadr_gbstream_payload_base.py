from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.feed import Feed
from trystructure_clusters.stream_payload_base_type import StreamPayloadBaseType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbstreamPayloadBase(StreamPayloadBaseType):
    class Meta:
        name = "oadrGBStreamPayloadBase"

    feed: Optional[Feed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "required": True,
        }
    )
