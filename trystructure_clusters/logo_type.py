from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class LogoType:
    """
    The Atom logo construct is defined in section 4.2.8 of the format spec.
    """
    class Meta:
        name = "logoType"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
