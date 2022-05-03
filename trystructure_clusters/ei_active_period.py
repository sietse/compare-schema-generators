from dataclasses import dataclass
from trystructure_clusters.ei_active_period_type import EiActivePeriodType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiActivePeriod(EiActivePeriodType):
    """
    Time frames relevant to the overall event.
    """
    class Meta:
        name = "eiActivePeriod"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
