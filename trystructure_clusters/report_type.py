from dataclasses import dataclass, field
from typing import Union
from trystructure_clusters.report_enumerated_type import ReportEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportType:
    class Meta:
        name = "reportType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReportEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
