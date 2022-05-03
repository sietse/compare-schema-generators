from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_profile_type import OadrProfileType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_transports import OadrTransports

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrProfiles:
    """
    OpenADR profiles supported by the implementation.
    """
    class Meta:
        name = "oadrProfiles"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_profile: List["OadrProfiles.OadrProfile"] = field(
        default_factory=list,
        metadata={
            "name": "oadrProfile",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class OadrProfile:
        oadr_profile_name: Optional[OadrProfileType] = field(
            default=None,
            metadata={
                "name": "oadrProfileName",
                "type": "Element",
                "required": True,
            }
        )
        oadr_transports: Optional[OadrTransports] = field(
            default=None,
            metadata={
                "name": "oadrTransports",
                "type": "Element",
                "required": True,
            }
        )
