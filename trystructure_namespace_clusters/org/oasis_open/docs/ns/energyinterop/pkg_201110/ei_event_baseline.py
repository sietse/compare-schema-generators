from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_event_baseline_type import EiEventBaselineType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventBaseline(EiEventBaselineType):
    """
    B profile.
    """
    class Meta:
        name = "eiEventBaseline"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
