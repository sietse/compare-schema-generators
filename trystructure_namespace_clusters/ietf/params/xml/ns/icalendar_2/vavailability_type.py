from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.array_of_vavailability_contained_components import ArrayOfVavailabilityContainedComponents

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class VavailabilityType:
    components: Optional[ArrayOfVavailabilityContainedComponents] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
