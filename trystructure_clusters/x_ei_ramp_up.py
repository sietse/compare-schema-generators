from dataclasses import dataclass
from trystructure_clusters.duration_prop_type import DurationPropType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class XEiRampUp(DurationPropType):
    """
    A duration before or after the event start time during which load shed
    should transit.
    """
    class Meta:
        name = "x-eiRampUp"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
