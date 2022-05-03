from dataclasses import dataclass, field

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class DateTime:
    class Meta:
        name = "date-time"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
