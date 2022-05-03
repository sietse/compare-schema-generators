from dataclasses import dataclass, field

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Text:
    class Meta:
        name = "text"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
