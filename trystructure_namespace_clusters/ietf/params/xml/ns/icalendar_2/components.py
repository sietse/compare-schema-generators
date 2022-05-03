from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Components:
    class Meta:
        name = "components"
        nillable = True
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
