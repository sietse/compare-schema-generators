from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"


@dataclass
class EiRequestEvent:
    """
    Request Event from a VTN in pull mode.

    :ivar request_id:
    :ivar ven_id:
    :ivar reply_limit: Limit the number of events contained in the
        oadrDistributeEvent payload
    """
    class Meta:
        name = "eiRequestEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "required": True,
        }
    )
    ven_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    reply_limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "replyLimit",
            "type": "Element",
        }
    )
