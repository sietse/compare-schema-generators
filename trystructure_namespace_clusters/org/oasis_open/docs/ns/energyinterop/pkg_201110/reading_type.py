from dataclasses import dataclass, field
from typing import Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.reading_type_enumerated_type import ReadingTypeEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReadingType:
    """
    Metadata about the Readings, such as mean or derived.
    """
    class Meta:
        name = "readingType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReadingTypeEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
