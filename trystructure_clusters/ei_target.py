from dataclasses import dataclass
from trystructure_clusters.ei_target_type import EiTargetType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiTarget(EiTargetType):
    """Identifies the resources associated with the logical VEN interface.

    For events, the values specified are the target for the event
    """
    class Meta:
        name = "eiTarget"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
