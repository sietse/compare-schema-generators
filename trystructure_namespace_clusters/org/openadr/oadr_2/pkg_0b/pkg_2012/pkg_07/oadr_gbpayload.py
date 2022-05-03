from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_gbstream_payload_base import OadrGbstreamPayloadBase

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbpayload(OadrGbstreamPayloadBase):
    class Meta:
        name = "oadrGBPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
