from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06"


@dataclass
class MarketContext:
    """
    A URI identifying a DR Program.
    """
    class Meta:
        name = "marketContext"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
