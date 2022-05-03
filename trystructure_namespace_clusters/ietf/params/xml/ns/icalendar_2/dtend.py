from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Dtend:
    class Meta:
        name = "dtend"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
