from dataclasses import dataclass
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.ws_calendar_interval_type import WsCalendarIntervalType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Interval(WsCalendarIntervalType):
    class Meta:
        name = "interval"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
