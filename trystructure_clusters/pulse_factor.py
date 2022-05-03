from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class PulseFactor:
    """
    kWh per count.
    """
    class Meta:
        name = "pulseFactor"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
