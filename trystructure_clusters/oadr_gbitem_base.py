from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.feed import Feed
from trystructure_clusters.item_base_type import ItemBaseType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbitemBase(ItemBaseType):
    class Meta:
        name = "oadrGBItemBase"

    feed: Optional[Feed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "required": True,
        }
    )
