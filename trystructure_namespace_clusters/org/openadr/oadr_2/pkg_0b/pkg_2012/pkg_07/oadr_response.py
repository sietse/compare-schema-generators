from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_response_type import OadrResponseType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrResponse(OadrResponseType):
    class Meta:
        name = "oadrResponse"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
