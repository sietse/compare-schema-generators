from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_event_type import EiEventType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEvent(EiEventType):
    class Meta:
        name = "eiEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
