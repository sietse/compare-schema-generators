from dataclasses import dataclass, field
from typing import Dict, List, Optional
from trystructure_clusters.category_type import CategoryType
from trystructure_clusters.content_type import ContentType
from trystructure_clusters.date_time_type import DateTimeType
from trystructure_clusters.id_type import IdType
from trystructure_clusters.link_type import LinkType
from trystructure_clusters.person_type import PersonType
from trystructure_clusters.text_type import TextType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class EntryType:
    """
    The Atom entry construct is defined in section 4.1.2 of the format spec.
    """
    class Meta:
        name = "entryType"

    author: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    content: List[ContentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    id: List[IdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    published: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    rights: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    source: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    summary: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    updated: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
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
