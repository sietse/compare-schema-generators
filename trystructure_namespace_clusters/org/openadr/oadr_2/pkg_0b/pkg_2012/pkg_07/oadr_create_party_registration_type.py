from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.registration_id import RegistrationId
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_profile_type import OadrProfileType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_transport_type import OadrTransportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatePartyRegistrationType:
    """
    :ivar request_id:
    :ivar registration_id: Used for re-registering an existing
        registration
    :ivar ven_id:
    :ivar oadr_profile_name:
    :ivar oadr_transport_name:
    :ivar oadr_transport_address: Address of this VEN. Not required if
        http pull model
    :ivar oadr_report_only: ReportOnlyDeviceFlag - True or False
    :ivar oadr_xml_signature: Implementation supports XML signatures -
        True or False
    :ivar oadr_ven_name: Human readable name for VEN
    :ivar oadr_http_pull_model: If transport is simpleHttp indicate if
        VEN is operating in pull exchange model - true or false
    :ivar schema_version:
    """
    class Meta:
        name = "oadrCreatePartyRegistrationType"

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
    oadr_profile_name: Optional[OadrProfileType] = field(
        default=None,
        metadata={
            "name": "oadrProfileName",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_transport_name: Optional[OadrTransportType] = field(
        default=None,
        metadata={
            "name": "oadrTransportName",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_transport_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrTransportAddress",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_report_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrReportOnly",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_xml_signature: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrXmlSignature",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_ven_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrVenName",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_http_pull_model: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrHttpPullModel",
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
