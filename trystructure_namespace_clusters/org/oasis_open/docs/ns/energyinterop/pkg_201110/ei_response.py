from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_response_type import EiResponseType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiResponse(EiResponseType):
    """
    Indicate whether received payload is acceptable.
    """
    class Meta:
        name = "eiResponse"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
