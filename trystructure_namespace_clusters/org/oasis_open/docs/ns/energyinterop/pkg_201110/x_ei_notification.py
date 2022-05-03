from dataclasses import dataclass
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration_prop_type import DurationPropType

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
