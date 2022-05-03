from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.key_info import KeyInfo
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.object_mod import Object
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signature_value import SignatureValue
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signed_info import SignedInfo

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureType:
    signed_info: Optional[SignedInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_value: Optional[SignatureValue] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    key_info: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    object_value: List[Object] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
