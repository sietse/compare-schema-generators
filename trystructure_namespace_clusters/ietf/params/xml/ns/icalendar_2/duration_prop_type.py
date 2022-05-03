from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class DurationPropType:
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )
