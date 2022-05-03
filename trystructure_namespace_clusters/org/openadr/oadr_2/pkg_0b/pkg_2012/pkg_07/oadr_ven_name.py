from dataclasses import dataclass, field

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrVenName:
    """VEN name.

    May be used in VTN GUI
    """
    class Meta:
        name = "oadrVenName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
