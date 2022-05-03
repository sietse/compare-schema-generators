from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ResponseCode:
    """
    A 3 digit response code.
    """
    class Meta:
        name = "responseCode"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9][0-9][0-9]",
        }
    )
