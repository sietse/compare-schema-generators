from dataclasses import dataclass
from trystructure_clusters.ei_event_baseline_type import EiEventBaselineType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventBaseline(EiEventBaselineType):
    """
    B profile.
    """
    class Meta:
        name = "eiEventBaseline"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
