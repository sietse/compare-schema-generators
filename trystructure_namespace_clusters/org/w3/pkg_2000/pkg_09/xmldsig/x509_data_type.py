from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.x509_issuer_serial_type import X509IssuerSerialType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509DataType:
    x509_issuer_serial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    x509_ski: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509SKI",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_subject_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "X509SubjectName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    x509_certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_crl: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509CRL",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )
