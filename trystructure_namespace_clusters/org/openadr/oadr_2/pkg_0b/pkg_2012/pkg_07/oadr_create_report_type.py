from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_report_request import OadrReportRequest

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreateReportType:
    """
    :ivar request_id:
    :ivar oadr_report_request: Request report
    :ivar ven_id:
    :ivar schema_version:
    """
    class Meta:
        name = "oadrCreateReportType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    oadr_report_request: List[OadrReportRequest] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportRequest",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "min_occurs": 1,
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
