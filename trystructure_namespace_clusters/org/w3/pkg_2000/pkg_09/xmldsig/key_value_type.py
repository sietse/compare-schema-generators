from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.dsakey_value import DsakeyValue
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.rsakey_value import RsakeyValue

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class KeyValueType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )
