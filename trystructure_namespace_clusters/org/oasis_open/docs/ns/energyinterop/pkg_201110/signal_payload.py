from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.signal_payload_type import SignalPayloadType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalPayload(SignalPayloadType):
    """
    Signal values for events and baselines.
    """
    class Meta:
        name = "signalPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
