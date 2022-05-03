from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_payload_resource_status_type import OadrPayloadResourceStatusType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayloadResourceStatus(OadrPayloadResourceStatusType):
    """
    Current resource status information.
    """
    class Meta:
        name = "oadrPayloadResourceStatus"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
