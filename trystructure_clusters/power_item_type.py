from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.item_base_type import ItemBaseType
from trystructure_clusters.power_attributes import PowerAttributes
from trystructure_clusters.si_scale_code_type import SiScaleCodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerItemType(ItemBaseType):
    """
    Base for the measurement of Power.
    """
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
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
    power_attributes: Optional[PowerAttributes] = field(
        default=None,
        metadata={
            "name": "powerAttributes",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
