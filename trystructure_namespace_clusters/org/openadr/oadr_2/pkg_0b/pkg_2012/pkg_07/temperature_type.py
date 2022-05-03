from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.item_base_type import ItemBaseType
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.siscale.si_scale_code_type import SiScaleCodeType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.temperature_unit_type import TemperatureUnitType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class TemperatureType(ItemBaseType):
    """
    temperature.

    :ivar item_description:
    :ivar item_units: Temperature in Celsius or Fahrenheit
    :ivar si_scale_code:
    """
    class Meta:
        name = "temperatureType"

    item_description: str = field(
        init=False,
        default="temperature",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: Optional[TemperatureUnitType] = field(
        default=None,
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
