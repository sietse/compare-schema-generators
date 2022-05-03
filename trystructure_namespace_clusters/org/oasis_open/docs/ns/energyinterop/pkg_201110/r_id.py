from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class RId:
    """
    ReferenceID for this data point.
    """
    class Meta:
        name = "rID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
