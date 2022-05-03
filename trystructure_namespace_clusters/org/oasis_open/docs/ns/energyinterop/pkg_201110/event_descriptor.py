from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.event_descriptor_type import EventDescriptorType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventDescriptor(EventDescriptorType):
    """
    Information about the event.
    """
    class Meta:
        name = "eventDescriptor"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
