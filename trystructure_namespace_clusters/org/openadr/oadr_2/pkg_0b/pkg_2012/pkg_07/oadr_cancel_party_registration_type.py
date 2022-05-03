from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.registration_id import RegistrationId
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelPartyRegistrationType:
    class Meta:
        name = "oadrCancelPartyRegistrationType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    registration_id: Optional[RegistrationId] = field(
        default=None,
        metadata={
            "name": "registrationID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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
