from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class CreatedDateTime:
    """
    The dateTime the payload was created.
    """
    class Meta:
        name = "createdDateTime"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
