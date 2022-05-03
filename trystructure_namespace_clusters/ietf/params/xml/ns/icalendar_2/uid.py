from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Uid:
    """
    Used as an index to identify intervals.
    """
    class Meta:
        name = "uid"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
