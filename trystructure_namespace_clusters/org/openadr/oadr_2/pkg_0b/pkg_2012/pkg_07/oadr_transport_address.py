from dataclasses import dataclass, field

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrTransportAddress:
    """Root address used to communicate with other party.

    Should include port if required
    """
    class Meta:
        name = "oadrTransportAddress"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
