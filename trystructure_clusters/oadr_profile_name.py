from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_profile_type import OadrProfileType

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
