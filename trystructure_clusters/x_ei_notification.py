from dataclasses import dataclass
from trystructure_clusters.duration_prop_type import DurationPropType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class XEiNotification(DurationPropType):
    """
    The VEN should receive the DR event payload prior to dtstart minus this
    duration.
    """
    class Meta:
        name = "x-eiNotification"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
