from dataclasses import dataclass, field
from typing import Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.report_name_enumerated_type import ReportNameEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportName:
    """
    Optional name for a report.
    """
    class Meta:
        name = "reportName"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReportNameEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
