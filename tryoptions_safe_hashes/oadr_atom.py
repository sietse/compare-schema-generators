from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, Tuple
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass(frozen=True)
class CategoryType:
    """
    The Atom category construct is defined in section 4.2.2 of the format spec.
    """
    class Meta:
        name = "categoryType"

    term: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
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


@dataclass(frozen=True)
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
    content: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass(frozen=True)
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


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class IconType:
    """
    The Atom icon construct is defined in section 4.2.5 of the format spec.
    """
    class Meta:
        name = "iconType"

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


@dataclass(frozen=True)
class IdType:
    """
    The Atom id construct is defined in section 4.2.6 of the format spec.
    """
    class Meta:
        name = "idType"

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


@dataclass(frozen=True)
class LinkType:
    """
    The Atom link construct is defined in section 3.4 of the format spec.
    """
    class Meta:
        name = "linkType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    length: Optional[int] = field(
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
    content: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass(frozen=True)
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


class TextTypeType(Enum):
    TEXT = "text"
    HTML = "html"
    XHTML = "xhtml"


@dataclass(frozen=True)
class UriType:
    class Meta:
        name = "uriType"

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


@dataclass(frozen=True)
class PersonType:
    """
    The Atom person construct is defined in section 3.2 of the format spec.
    """
    class Meta:
        name = "personType"

    choice: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "name",
                    "type": str,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "uri",
                    "type": UriType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "email",
                    "type": str,
                    "namespace": "http://www.w3.org/2005/Atom",
                    "pattern": r"\w+@(\w+\.)+\w+",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
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


@dataclass(frozen=True)
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
    content: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass(frozen=True)
class EntryType:
    """
    The Atom entry construct is defined in section 4.1.2 of the format spec.
    """
    class Meta:
        name = "entryType"

    choice: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "author",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "category",
                    "type": CategoryType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "content",
                    "type": ContentType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "contributor",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "id",
                    "type": IdType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "link",
                    "type": LinkType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "published",
                    "type": DateTimeType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "rights",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "source",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "summary",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "title",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "updated",
                    "type": DateTimeType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
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


@dataclass(frozen=True)
class SourceType:
    """
    The Atom source construct is defined in section 4.2.11 of the format spec.
    """
    class Meta:
        name = "sourceType"

    choice: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "author",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "category",
                    "type": CategoryType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "contributor",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "generator",
                    "type": GeneratorType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "icon",
                    "type": IconType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "id",
                    "type": IdType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "link",
                    "type": LinkType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "logo",
                    "type": LogoType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "rights",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "subtitle",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "title",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "updated",
                    "type": DateTimeType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
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


@dataclass(frozen=True)
class Entry(EntryType):
    class Meta:
        name = "entry"
        namespace = "http://www.w3.org/2005/Atom"


@dataclass(frozen=True)
class FeedType:
    """
    The Atom feed construct is defined in section 4.1.1 of the format spec.
    """
    class Meta:
        name = "feedType"

    choice: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "author",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "category",
                    "type": CategoryType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "contributor",
                    "type": PersonType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "generator",
                    "type": GeneratorType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "icon",
                    "type": IconType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "id",
                    "type": IdType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "link",
                    "type": LinkType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "logo",
                    "type": LogoType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "rights",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "subtitle",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "title",
                    "type": TextType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "updated",
                    "type": DateTimeType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "name": "entry",
                    "type": EntryType,
                    "namespace": "http://www.w3.org/2005/Atom",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
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


@dataclass(frozen=True)
class Feed(FeedType):
    class Meta:
        name = "feed"
        namespace = "http://www.w3.org/2005/Atom"
