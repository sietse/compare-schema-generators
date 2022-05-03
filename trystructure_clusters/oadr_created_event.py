from dataclasses import dataclass
from trystructure_clusters.oadr_created_event_type import OadrCreatedEventType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedEvent(OadrCreatedEventType):
    class Meta:
        name = "oadrCreatedEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
