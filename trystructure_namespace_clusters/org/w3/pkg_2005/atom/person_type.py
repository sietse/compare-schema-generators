from dataclasses import dataclass, field
from typing import Dict, List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.uri_type import UriType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class PersonType:
    """
    The Atom person construct is defined in section 3.2 of the format spec.
    """
    class Meta:
        name = "personType"

    name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    uri: List[UriType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "pattern": r"\w+@(\w+\.)+\w+",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
