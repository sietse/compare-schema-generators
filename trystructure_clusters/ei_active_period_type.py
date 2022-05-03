from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.components import Components
from trystructure_clusters.properties import Properties

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiActivePeriodType:
    class Meta:
        name = "eiActivePeriodType"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    components: Optional[Components] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "nillable": True,
        }
    )
