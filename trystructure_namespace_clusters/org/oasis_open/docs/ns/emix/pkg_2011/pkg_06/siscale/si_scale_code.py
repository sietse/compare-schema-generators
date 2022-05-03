from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.siscale.si_scale_code_type import SiScaleCodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/siscale"


@dataclass
class SiScaleCode:
    class Meta:
        name = "siScaleCode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/siscale"

    value: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
