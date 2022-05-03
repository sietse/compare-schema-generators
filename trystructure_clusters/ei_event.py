from dataclasses import dataclass
from trystructure_clusters.ei_event_type import EiEventType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEvent(EiEventType):
    class Meta:
        name = "eiEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
