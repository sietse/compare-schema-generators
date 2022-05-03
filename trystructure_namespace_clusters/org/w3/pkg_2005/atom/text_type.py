from dataclasses import dataclass, field
from typing import Dict, List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.text_type_type import TextTypeType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class TextType:
    """
    The Atom text construct is defined in section 3.1 of the format spec.
    """
    class Meta:
        name = "textType"

    type: Optional[TextTypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
