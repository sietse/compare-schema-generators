from dataclasses import dataclass
from trystructure_clusters.oadr_gbstream_payload_base import OadrGbstreamPayloadBase

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbpayload(OadrGbstreamPayloadBase):
    class Meta:
        name = "oadrGBPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
