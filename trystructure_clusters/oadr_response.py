from dataclasses import dataclass
from trystructure_clusters.oadr_response_type import OadrResponseType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrResponse(OadrResponseType):
    class Meta:
        name = "oadrResponse"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
