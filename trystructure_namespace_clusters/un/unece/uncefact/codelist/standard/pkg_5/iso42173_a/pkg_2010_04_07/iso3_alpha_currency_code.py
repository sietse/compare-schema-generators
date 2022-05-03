from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.un.unece.uncefact.codelist.standard.pkg_5.iso42173_a.pkg_2010_04_07.iso3_alpha_currency_code_content_type import Iso3AlphaCurrencyCodeContentType

__NAMESPACE__ = "urn:un:unece:uncefact:codelist:standard:5:ISO42173A:2010-04-07"


@dataclass
class Iso3AlphaCurrencyCode:
    class Meta:
        name = "ISO3AlphaCurrencyCode"
        namespace = "urn:un:unece:uncefact:codelist:standard:5:ISO42173A:2010-04-07"

    value: Optional[Iso3AlphaCurrencyCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
