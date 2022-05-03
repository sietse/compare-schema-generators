from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.available import Available

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class ArrayOfVavailabilityContainedComponents:
    available: List[Available] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
