from dataclasses import dataclass
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration_prop_type import DurationPropType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Granularity(DurationPropType):
    class Meta:
        name = "granularity"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
