from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class GeneratorType:
    """
    The Atom generator element is defined in section 4.2.4 of the format spec.
    """
    class Meta:
        name = "generatorType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
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
