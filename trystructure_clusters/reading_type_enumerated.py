from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.reading_type_enumerated_type import ReadingTypeEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReadingTypeEnumerated:
    class Meta:
        name = "readingTypeEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[ReadingTypeEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
