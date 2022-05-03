from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespaces.org.oasis_open.docs.ns.energyinterop.mod_201110 import (
    EiResponse,
    EventResponses,
)

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


@dataclass
class ReplyLimit:
    class Meta:
        name = "replyLimit"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


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


@dataclass
class RequestId:
    """
    A ID used to match up a logical transaction request and response.
    """
    class Meta:
        name = "requestID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class EiCreatedEvent:
    """
    Respond to a DR Event with optIn or optOut.
    """
    class Meta:
        name = "eiCreatedEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    event_responses: Optional[EventResponses] = field(
        default=None,
        metadata={
            "name": "eventResponses",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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
