from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ReadingInterharmonic:
    """
    [extension] Interharmonics are represented as a rational number 'numerator'
    / 'denominator', and harmonics are represented using the same mechanism and
    identified by 'denominator'=1.
    """
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
