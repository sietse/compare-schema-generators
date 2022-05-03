from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelReportType:
    class Meta:
        name = "oadrCancelReportType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    report_request_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
    report_to_follow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reportToFollow",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    ven_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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
