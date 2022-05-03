from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_profile_type import OadrProfileType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrProfileName:
    """
    OpenADR profile name such as 2.0a or 2.0b.
    """
    class Meta:
        name = "oadrProfileName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrProfileType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
