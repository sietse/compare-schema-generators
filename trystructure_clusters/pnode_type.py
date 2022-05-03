from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PnodeType:
    """A pricing node is directly associated with a connectivity node.

    It is a pricing location for which market participants submit their
    bids, offers, buy/sell CRRs, and settle.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
