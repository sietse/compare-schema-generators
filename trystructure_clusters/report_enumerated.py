from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.report_enumerated_type import ReportEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportEnumerated:
    class Meta:
        name = "reportEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[ReportEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
