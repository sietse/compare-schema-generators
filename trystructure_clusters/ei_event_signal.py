from dataclasses import dataclass
from trystructure_clusters.ei_event_signal_type import EiEventSignalType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignal(EiEventSignalType):
    class Meta:
        name = "eiEventSignal"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
