from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.currency_item_description_type import CurrencyItemDescriptionType
from trystructure_clusters.iso3_alpha_currency_code_content_type import Iso3AlphaCurrencyCodeContentType
from trystructure_clusters.item_base_type import ItemBaseType
from trystructure_clusters.si_scale_code_type import SiScaleCodeType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyType(ItemBaseType):
    """
    currency.

    :ivar item_description:
    :ivar item_units: ISO enumeration of currency types, such as USD
    :ivar si_scale_code:
    """
    class Meta:
        name = "currencyType"

    item_description: Optional[CurrencyItemDescriptionType] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: Optional[Iso3AlphaCurrencyCodeContentType] = field(
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
