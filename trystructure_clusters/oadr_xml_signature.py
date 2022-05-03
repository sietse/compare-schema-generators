from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrXmlSignature:
    """
    Implementation supports XML signature.
    """
    class Meta:
        name = "oadrXmlSignature"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
