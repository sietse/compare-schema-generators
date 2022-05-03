from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"


@dataclass
class RequestId:
    """
    A ID used to match up a logical transaction request and response.
    """
    class Meta:
        name = "requestID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
