from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.item_base_type import ItemBaseType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.siscale.si_scale_code_type import SiScaleCodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyItemType(ItemBaseType):
    """
    Base for the measurement of Energy.
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
