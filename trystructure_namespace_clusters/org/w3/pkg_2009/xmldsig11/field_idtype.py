from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.gn_b import GnB
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.pn_b import PnB
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.prime import Prime
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.tn_b import TnB

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class FieldIdtype:
    class Meta:
        name = "FieldIDType"

    prime: Optional[Prime] = field(
        default=None,
        metadata={
            "name": "Prime",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    tn_b: Optional[TnB] = field(
        default=None,
        metadata={
            "name": "TnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    pn_b: Optional[PnB] = field(
        default=None,
        metadata={
            "name": "PnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    gn_b: Optional[GnB] = field(
        default=None,
        metadata={
            "name": "GnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
