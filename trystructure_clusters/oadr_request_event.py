from dataclasses import dataclass
from trystructure_clusters.oadr_request_event_type import OadrRequestEventType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestEvent(OadrRequestEventType):
    class Meta:
        name = "oadrRequestEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
