from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventId:
    """
    An ID value that identifies a specific DR event instance.
    """
    class Meta:
        name = "eventID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
