from dataclasses import dataclass
from trystructure_clusters.oadr_payload_resource_status_type import OadrPayloadResourceStatusType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayloadResourceStatus(OadrPayloadResourceStatusType):
    """
    Current resource status information.
    """
    class Meta:
        name = "oadrPayloadResourceStatus"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
