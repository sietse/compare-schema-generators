from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.pkg_0.stream.stream_payload_base_type import StreamPayloadBaseType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.feed import Feed

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
