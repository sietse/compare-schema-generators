from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.canonicalization_method import CanonicalizationMethod
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.reference import Reference
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.signature_method import SignatureMethod

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignedInfoType:
    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
