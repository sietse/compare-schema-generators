from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"


@dataclass
class ReportToFollow:
    """
    Indicates if report (in the form of UpdateReport) to be returned following
    cancellation of Report.
    """
    class Meta:
        name = "reportToFollow"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
