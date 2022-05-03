from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class RationalNumber:
    """[extension] Rational number = 'numerator' / 'denominator'."""
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
