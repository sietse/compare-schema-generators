from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PosList:
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
