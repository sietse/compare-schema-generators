from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class VenId:
    class Meta:
        name = "venID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
