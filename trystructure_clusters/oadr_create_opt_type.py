from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.ei_opt_type import EiOptType
from trystructure_clusters.ei_target import EiTarget
from trystructure_clusters.oadr_device_class import OadrDeviceClass
from trystructure_clusters.qualified_event_id import QualifiedEventId

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreateOptType(EiOptType):
    class Meta:
        name = "oadrCreateOptType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    qualified_event_id: Optional[QualifiedEventId] = field(
        default=None,
        metadata={
            "name": "qualifiedEventID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ei_target: Optional[EiTarget] = field(
        default=None,
        metadata={
            "name": "eiTarget",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_device_class: Optional[OadrDeviceClass] = field(
        default=None,
        metadata={
            "name": "oadrDeviceClass",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
