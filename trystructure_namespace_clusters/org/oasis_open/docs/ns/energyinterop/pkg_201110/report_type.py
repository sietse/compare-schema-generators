from dataclasses import dataclass, field
from typing import Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.report_enumerated_type import ReportEnumeratedType

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
