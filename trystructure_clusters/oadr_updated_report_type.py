from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.ei_response import EiResponse
from trystructure_clusters.oadr_cancel_report import OadrCancelReport
from trystructure_clusters.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdatedReportType:
    class Meta:
        name = "oadrUpdatedReportType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_cancel_report: Optional[OadrCancelReport] = field(
        default=None,
        metadata={
            "name": "oadrCancelReport",
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
    schema_version: Optional[Union[SchemaVersionEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"x-\S.*",
        }
    )
