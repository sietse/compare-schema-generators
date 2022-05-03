from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.digest_method import DigestMethod
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.transforms import Transforms

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ReferenceType:
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
