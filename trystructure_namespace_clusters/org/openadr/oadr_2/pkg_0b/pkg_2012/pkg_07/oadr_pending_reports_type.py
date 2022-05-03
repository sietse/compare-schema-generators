from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPendingReportsType:
    class Meta:
        name = "oadrPendingReportsType"

    report_request_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
