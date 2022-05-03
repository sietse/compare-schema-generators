from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class AggregatedPnodeType:
    """
    An aggregated pricing node is a specialized type of pricing node used to
    model items such as System Zone, Default Price Zone, Custom Price Zone,
    Control Area, Aggregated Generation, Aggregated Participating Load,
    Aggregated Non-Participating Load, Trading Hub, DCA Zone.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
