from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class ContentType:
    """
    The Atom content construct is defined in section 4.1.3 of the format spec.
    """
    class Meta:
        name = "contentType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
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
