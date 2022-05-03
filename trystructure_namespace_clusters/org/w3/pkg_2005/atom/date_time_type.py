from dataclasses import dataclass, field
from typing import Dict, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class DateTimeType:
    class Meta:
        name = "dateTimeType"

    value: Optional[XmlDateTime] = field(
        default=None,
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
