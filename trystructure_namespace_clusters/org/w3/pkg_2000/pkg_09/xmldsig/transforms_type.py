from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.transform import Transform

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TransformsType:
    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
