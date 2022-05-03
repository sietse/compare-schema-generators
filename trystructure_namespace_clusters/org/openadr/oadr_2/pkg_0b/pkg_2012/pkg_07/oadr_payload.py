from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_signed_object import OadrSignedObject
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signature import Signature

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
