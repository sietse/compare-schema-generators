from dataclasses import dataclass
from trystructure_clusters.event_descriptor_type import EventDescriptorType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventDescriptor(EventDescriptorType):
    """
    Information about the event.
    """
    class Meta:
        name = "eventDescriptor"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
