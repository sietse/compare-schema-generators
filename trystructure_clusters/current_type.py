from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.item_base_type import ItemBaseType
from trystructure_clusters.si_scale_code_type import SiScaleCodeType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrentType(ItemBaseType):
    """
    Current.
    """
    item_description: str = field(
        init=False,
        default="Current",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="A",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )
