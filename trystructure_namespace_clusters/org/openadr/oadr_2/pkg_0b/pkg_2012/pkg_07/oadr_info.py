from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrInfo:
    """
    A key value pair of service specific registration information.
    """
    class Meta:
        name = "oadrInfo"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrKey",
            "type": "Element",
            "required": True,
        }
    )
    oadr_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrValue",
            "type": "Element",
            "required": True,
        }
    )
