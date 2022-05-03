from dataclasses import dataclass
from trystructure_clusters.duration_prop_type import DurationPropType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Duration(DurationPropType):
    """
    The duration of the  activity, data, or state.
    """
    class Meta:
        name = "duration"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
