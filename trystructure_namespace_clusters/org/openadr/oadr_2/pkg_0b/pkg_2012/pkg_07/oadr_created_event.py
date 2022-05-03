from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_created_event_type import OadrCreatedEventType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedEvent(OadrCreatedEventType):
    class Meta:
        name = "oadrCreatedEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
