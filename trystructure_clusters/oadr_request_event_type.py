from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.ei_request_event import EiRequestEvent
from trystructure_clusters.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestEventType:
    class Meta:
        name = "oadrRequestEventType"

    ei_request_event: Optional[EiRequestEvent] = field(
        default=None,
        metadata={
            "name": "eiRequestEvent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
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
