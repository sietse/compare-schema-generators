from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_event import EiEvent
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_response import EiResponse
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.response_required_type import ResponseRequiredType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDistributeEventType:
    """
    :ivar ei_response:
    :ivar request_id:
    :ivar vtn_id:
    :ivar oadr_event: An object containing a demand response event
    :ivar schema_version:
    """
    class Meta:
        name = "oadrDistributeEventType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
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
    vtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtnID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_event: List["OadrDistributeEventType.OadrEvent"] = field(
        default_factory=list,
        metadata={
            "name": "oadrEvent",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    schema_version: Optional[Union[SchemaVersionEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"x-\S.*",
        }
    )

    @dataclass
    class OadrEvent:
        ei_event: Optional[EiEvent] = field(
            default=None,
            metadata={
                "name": "eiEvent",
                "type": "Element",
                "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
                "required": True,
            }
        )
        oadr_response_required: Optional[ResponseRequiredType] = field(
            default=None,
            metadata={
                "name": "oadrResponseRequired",
                "type": "Element",
                "namespace": "http://openadr.org/oadr-2.0b/2012/07",
                "required": True,
            }
        )
