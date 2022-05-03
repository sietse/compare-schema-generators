from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class Object1:
    """
    Superclass of all object classes to allow extensions.

    :ivar extension: Contains an extension.
    """
    class Meta:
        name = "Object"
        namespace = "http://naesb.org/espi"

    extension: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
