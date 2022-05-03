from dataclasses import dataclass
from trystructure_clusters.ws_calendar_interval_type import WsCalendarIntervalType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Interval1(WsCalendarIntervalType):
    class Meta:
        name = "interval"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
