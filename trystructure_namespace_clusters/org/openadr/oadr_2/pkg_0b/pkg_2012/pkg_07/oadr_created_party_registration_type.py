from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_response import EiResponse
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.registration_id import RegistrationId
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.schema_version_enumerated_type import SchemaVersionEnumeratedType
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_info import OadrInfo
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_profiles import OadrProfiles
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_requested_oadr_poll_freq import OadrRequestedOadrPollFreq
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_service_specific_info import OadrServiceSpecificInfo

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedPartyRegistrationType:
    """
    :ivar ei_response:
    :ivar registration_id:
    :ivar ven_id: venID not included in query unless already registered
    :ivar vtn_id:
    :ivar oadr_profiles: VTN response to query registration returns all
        supported. This element is not required for a registration
        response
    :ivar oadr_requested_oadr_poll_freq: HTTP Pull Only - The VEN shall
        send an oadrPoll payload to the VTN at most once for each
        duration specified by this element
    :ivar oadr_service_specific_info:
    :ivar oadr_extensions:
    :ivar schema_version:
    """
    class Meta:
        name = "oadrCreatedPartyRegistrationType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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
    vtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtnID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_profiles: Optional[OadrProfiles] = field(
        default=None,
        metadata={
            "name": "oadrProfiles",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_requested_oadr_poll_freq: Optional[OadrRequestedOadrPollFreq] = field(
        default=None,
        metadata={
            "name": "oadrRequestedOadrPollFreq",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_service_specific_info: Optional[OadrServiceSpecificInfo] = field(
        default=None,
        metadata={
            "name": "oadrServiceSpecificInfo",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_extensions: Optional["OadrCreatedPartyRegistrationType.OadrExtensions"] = field(
        default=None,
        metadata={
            "name": "oadrExtensions",
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

    @dataclass
    class OadrExtensions:
        oadr_extension: List["OadrCreatedPartyRegistrationType.OadrExtensions.OadrExtension"] = field(
            default_factory=list,
            metadata={
                "name": "oadrExtension",
                "type": "Element",
                "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            }
        )

        @dataclass
        class OadrExtension:
            oadr_extension_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "oadrExtensionName",
                    "type": "Element",
                    "namespace": "http://openadr.org/oadr-2.0b/2012/07",
                    "required": True,
                }
            )
            oadr_info: List[OadrInfo] = field(
                default_factory=list,
                metadata={
                    "name": "oadrInfo",
                    "type": "Element",
                    "namespace": "http://openadr.org/oadr-2.0b/2012/07",
                }
            )
