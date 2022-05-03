from dataclasses import dataclass
from trystructure_clusters.ei_response_type import EiResponseType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiResponse(EiResponseType):
    """
    Indicate whether received payload is acceptable.
    """
    class Meta:
        name = "eiResponse"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
