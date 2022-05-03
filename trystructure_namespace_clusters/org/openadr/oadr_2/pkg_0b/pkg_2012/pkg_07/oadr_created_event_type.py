from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.payloads.ei_created_event import EiCreatedEvent
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedEventType:
    class Meta:
        name = "oadrCreatedEventType"

    ei_created_event: Optional[EiCreatedEvent] = field(
        default=None,
        metadata={
            "name": "eiCreatedEvent",
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
