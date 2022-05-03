from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_signed_object import OadrSignedObject
from trystructure_clusters.signature import Signature

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayload:
    class Meta:
        name = "oadrPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    oadr_signed_object: Optional[OadrSignedObject] = field(
        default=None,
        metadata={
            "name": "oadrSignedObject",
            "type": "Element",
            "required": True,
        }
    )
