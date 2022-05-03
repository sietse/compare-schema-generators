from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.ei_response import EiResponse
from trystructure_clusters.oadr_pending_reports import OadrPendingReports
from trystructure_clusters.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedReportType:
    """
    :ivar ei_response:
    :ivar oadr_pending_reports: List of periodic reports that have not
        yet been delivered
    :ivar ven_id:
    :ivar schema_version:
    """
    class Meta:
        name = "oadrCreatedReportType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_pending_reports: Optional[OadrPendingReports] = field(
        default=None,
        metadata={
            "name": "oadrPendingReports",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
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
