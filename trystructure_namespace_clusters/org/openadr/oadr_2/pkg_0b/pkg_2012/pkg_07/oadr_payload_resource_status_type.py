from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.payload_base_type import PayloadBaseType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_load_control_state import OadrLoadControlState

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayloadResourceStatusType(PayloadBaseType):
    """
    This is the payload for reports that require a status.

    :ivar oadr_online: If true then resource/asset is online, if false
        then offline.
    :ivar oadr_manual_override: If true then the control of the load has
        been manually overridden
    :ivar oadr_load_control_state:
    """
    class Meta:
        name = "oadrPayloadResourceStatusType"

    oadr_online: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrOnline",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_manual_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrManualOverride",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_load_control_state: Optional[OadrLoadControlState] = field(
        default=None,
        metadata={
            "name": "oadrLoadControlState",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
