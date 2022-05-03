from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.key_value import KeyValue
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.pgpdata import Pgpdata
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.retrieval_method import RetrievalMethod
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.spkidata import Spkidata
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.x509_data import X509Data

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class KeyInfoType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KeyName",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )
