from dataclasses import dataclass
from trystructure_clusters.ei_event_signals_type import EiEventSignalsType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignals(EiEventSignalsType):
    """
    Interval data for one or more event signals and/or baselines.
    """
    class Meta:
        name = "eiEventSignals"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
