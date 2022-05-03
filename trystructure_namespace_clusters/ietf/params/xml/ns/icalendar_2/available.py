from dataclasses import dataclass
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.available_type import AvailableType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Available(AvailableType):
    class Meta:
        name = "available"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
