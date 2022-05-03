from dataclasses import dataclass, field
from typing import Dict, List, Optional
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.category_type import CategoryType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.date_time_type import DateTimeType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.generator_type import GeneratorType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.icon_type import IconType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.id_type import IdType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.link_type import LinkType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.logo_type import LogoType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.person_type import PersonType
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.text_type import TextType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class SourceType:
    """
    The Atom source construct is defined in section 4.2.11 of the format spec.
    """
    class Meta:
        name = "sourceType"

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
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    generator: List[GeneratorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    icon: List[IconType] = field(
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
    logo: List[LogoType] = field(
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
    subtitle: List[TextType] = field(
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
