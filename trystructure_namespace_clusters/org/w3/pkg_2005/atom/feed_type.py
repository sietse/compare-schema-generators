from dataclasses import dataclass, field
from typing import Dict, List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.category_type import CategoryType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.date_time_type import DateTimeType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.entry_type import EntryType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.generator_type import GeneratorType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.icon_type import IconType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.id_type import IdType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.link_type import LinkType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.logo_type import LogoType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.person_type import PersonType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.text_type import TextType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class FeedType:
    """
    The Atom feed construct is defined in section 4.1.1 of the format spec.
    """
    class Meta:
        name = "feedType"

    author: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    generator: List[GeneratorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    icon: List[IconType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    id: List[IdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    logo: List[LogoType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    rights: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    subtitle: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    updated: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    entry: List[EntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "min_occurs": 3,
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
