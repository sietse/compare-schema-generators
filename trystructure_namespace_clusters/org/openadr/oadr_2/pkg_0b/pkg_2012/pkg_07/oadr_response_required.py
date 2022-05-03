from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.response_required_type import ResponseRequiredType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrResponseRequired:
    """Controls when optIn/optOut repsonse is required.

    Can be always or never
    """
    class Meta:
        name = "oadrResponseRequired"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[ResponseRequiredType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
