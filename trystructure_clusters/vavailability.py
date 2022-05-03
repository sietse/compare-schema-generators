from dataclasses import dataclass
from trystructure_clusters.vavailability_type import VavailabilityType

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Vavailability(VavailabilityType):
    """
    A schedule reflecting device availability for participating in DR events.
    """
    class Meta:
        name = "vavailability"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
