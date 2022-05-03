from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class Object:
    """
    Superclass of all object classes to allow extensions.

    :ivar extension: Contains an extension.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    extension: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
