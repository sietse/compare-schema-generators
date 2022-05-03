from dataclasses import dataclass
from trystructure_clusters.signal_payload_type import SignalPayloadType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalPayload(SignalPayloadType):
    """
    Signal values for events and baselines.
    """
    class Meta:
        name = "signalPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
