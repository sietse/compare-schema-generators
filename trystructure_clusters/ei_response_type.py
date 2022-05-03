from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiResponseType:
    response_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "responseCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"[0-9][0-9][0-9]",
        }
    )
    response_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "responseDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
