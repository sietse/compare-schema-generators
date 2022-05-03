from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_cancel_opt import OadrCancelOpt
from trystructure_clusters.oadr_cancel_party_registration import OadrCancelPartyRegistration
from trystructure_clusters.oadr_cancel_report import OadrCancelReport
from trystructure_clusters.oadr_canceled_opt import OadrCanceledOpt
from trystructure_clusters.oadr_canceled_party_registration import OadrCanceledPartyRegistration
from trystructure_clusters.oadr_canceled_report import OadrCanceledReport
from trystructure_clusters.oadr_create_opt import OadrCreateOpt
from trystructure_clusters.oadr_create_party_registration import OadrCreatePartyRegistration
from trystructure_clusters.oadr_create_report import OadrCreateReport
from trystructure_clusters.oadr_created_event import OadrCreatedEvent
from trystructure_clusters.oadr_created_opt import OadrCreatedOpt
from trystructure_clusters.oadr_created_party_registration import OadrCreatedPartyRegistration
from trystructure_clusters.oadr_created_report import OadrCreatedReport
from trystructure_clusters.oadr_distribute_event import OadrDistributeEvent
from trystructure_clusters.oadr_poll import OadrPoll
from trystructure_clusters.oadr_query_registration import OadrQueryRegistration
from trystructure_clusters.oadr_register_report import OadrRegisterReport
from trystructure_clusters.oadr_registered_report import OadrRegisteredReport
from trystructure_clusters.oadr_request_event import OadrRequestEvent
from trystructure_clusters.oadr_request_reregistration import OadrRequestReregistration
from trystructure_clusters.oadr_response import OadrResponse
from trystructure_clusters.oadr_update_report import OadrUpdateReport
from trystructure_clusters.oadr_updated_report import OadrUpdatedReport

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrSignedObject:
    class Meta:
        name = "oadrSignedObject"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_distribute_event: Optional[OadrDistributeEvent] = field(
        default=None,
        metadata={
            "name": "oadrDistributeEvent",
            "type": "Element",
        }
    )
    oadr_created_event: Optional[OadrCreatedEvent] = field(
        default=None,
        metadata={
            "name": "oadrCreatedEvent",
            "type": "Element",
        }
    )
    oadr_request_event: Optional[OadrRequestEvent] = field(
        default=None,
        metadata={
            "name": "oadrRequestEvent",
            "type": "Element",
        }
    )
    oadr_response: Optional[OadrResponse] = field(
        default=None,
        metadata={
            "name": "oadrResponse",
            "type": "Element",
        }
    )
    oadr_cancel_opt: Optional[OadrCancelOpt] = field(
        default=None,
        metadata={
            "name": "oadrCancelOpt",
            "type": "Element",
        }
    )
    oadr_canceled_opt: Optional[OadrCanceledOpt] = field(
        default=None,
        metadata={
            "name": "oadrCanceledOpt",
            "type": "Element",
        }
    )
    oadr_create_opt: Optional[OadrCreateOpt] = field(
        default=None,
        metadata={
            "name": "oadrCreateOpt",
            "type": "Element",
        }
    )
    oadr_created_opt: Optional[OadrCreatedOpt] = field(
        default=None,
        metadata={
            "name": "oadrCreatedOpt",
            "type": "Element",
        }
    )
    oadr_cancel_report: Optional[OadrCancelReport] = field(
        default=None,
        metadata={
            "name": "oadrCancelReport",
            "type": "Element",
        }
    )
    oadr_canceled_report: Optional[OadrCanceledReport] = field(
        default=None,
        metadata={
            "name": "oadrCanceledReport",
            "type": "Element",
        }
    )
    oadr_create_report: Optional[OadrCreateReport] = field(
        default=None,
        metadata={
            "name": "oadrCreateReport",
            "type": "Element",
        }
    )
    oadr_created_report: Optional[OadrCreatedReport] = field(
        default=None,
        metadata={
            "name": "oadrCreatedReport",
            "type": "Element",
        }
    )
    oadr_register_report: Optional[OadrRegisterReport] = field(
        default=None,
        metadata={
            "name": "oadrRegisterReport",
            "type": "Element",
        }
    )
    oadr_registered_report: Optional[OadrRegisteredReport] = field(
        default=None,
        metadata={
            "name": "oadrRegisteredReport",
            "type": "Element",
        }
    )
    oadr_update_report: Optional[OadrUpdateReport] = field(
        default=None,
        metadata={
            "name": "oadrUpdateReport",
            "type": "Element",
        }
    )
    oadr_updated_report: Optional[OadrUpdatedReport] = field(
        default=None,
        metadata={
            "name": "oadrUpdatedReport",
            "type": "Element",
        }
    )
    oadr_cancel_party_registration: Optional[OadrCancelPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCancelPartyRegistration",
            "type": "Element",
        }
    )
    oadr_canceled_party_registration: Optional[OadrCanceledPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCanceledPartyRegistration",
            "type": "Element",
        }
    )
    oadr_create_party_registration: Optional[OadrCreatePartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCreatePartyRegistration",
            "type": "Element",
        }
    )
    oadr_created_party_registration: Optional[OadrCreatedPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCreatedPartyRegistration",
            "type": "Element",
        }
    )
    oadr_request_reregistration: Optional[OadrRequestReregistration] = field(
        default=None,
        metadata={
            "name": "oadrRequestReregistration",
            "type": "Element",
        }
    )
    oadr_query_registration: Optional[OadrQueryRegistration] = field(
        default=None,
        metadata={
            "name": "oadrQueryRegistration",
            "type": "Element",
        }
    )
    oadr_poll: Optional[OadrPoll] = field(
        default=None,
        metadata={
            "name": "oadrPoll",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
