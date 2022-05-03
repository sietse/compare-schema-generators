from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.opt_reason_enumerated_type import OptReasonEnumeratedType
from trystructure_clusters.opt_type_type import OptTypeType
from trystructure_clusters.schema_version_enumerated_type import SchemaVersionEnumeratedType
from trystructure_clusters.vavailability import Vavailability

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiOptType:
    """Opts are used by the VEN to temporarily override the pre-existing
    agreement.

    For example, a VEN may opt in to events during the evening, or opt
    out from events during the world series.
    """
    opt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "optID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    opt_type: Optional[OptTypeType] = field(
        default=None,
        metadata={
            "name": "optType",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    opt_reason: Optional[Union[OptReasonEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "optReason",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"x-\S.*",
        }
    )
    market_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketContext",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06",
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
    vavailability: Optional[Vavailability] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    created_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
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
