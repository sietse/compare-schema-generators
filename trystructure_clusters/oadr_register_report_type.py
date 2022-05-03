from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_clusters.oadr_report import OadrReport
from trystructure_clusters.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRegisterReportType:
    class Meta:
        name = "oadrRegisterReportType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    oadr_report: List[OadrReport] = field(
        default_factory=list,
        metadata={
            "name": "oadrReport",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
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
    report_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportRequestID",
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
