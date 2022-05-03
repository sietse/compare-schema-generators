from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from trystructure_filenames.oadr_atom import Feed
from trystructure_filenames.oadr_ei_20b import (
    EiOptType,
    EiTargetType,
    PayloadBaseType,
    ReadingTypeEnumeratedType,
    ReportEnumeratedType,
    ReportPayloadType,
    EiEvent,
    EiResponse,
    EiTarget,
    QualifiedEventId,
    RegistrationId,
    ReportDataSource,
    ReportNameEnumeratedType,
    ReportSpecifier,
    ReportSubject,
    SchemaVersionEnumeratedType,
)
from trystructure_filenames.oadr_emix_20b import ItemBaseType
from trystructure_filenames.oadr_iso_iso3_alpha_currency_code_20100407 import Iso3AlphaCurrencyCodeContentType
from trystructure_filenames.oadr_power_20b import (
    EnergyApparent,
    EnergyItem,
    EnergyReactive,
    EnergyReal,
    PowerApparent,
    PowerItem,
    PowerReactive,
    PowerReal,
    Voltage,
)
from trystructure_filenames.oadr_pyld_20b import (
    EiCreatedEvent,
    EiRequestEvent,
)
from trystructure_filenames.oadr_siscale_20b import SiScaleCodeType
from trystructure_filenames.oadr_strm_20b import (
    StreamBaseType,
    StreamPayloadBaseType,
)
from trystructure_filenames.oadr_xcal_20b import DurationPropType
from trystructure_filenames.oadr_xmldsig import Signature

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class ResponseRequiredType(Enum):
    """
    Defines what type of response is required.

    :cvar ALWAYS: Always send a response for every event received.
    :cvar NEVER: Never respond.
    """
    ALWAYS = "always"
    NEVER = "never"


class CurrencyItemDescriptionType(Enum):
    CURRENCY = "currency"
    CURRENCY_PER_KW = "currencyPerKW"
    CURRENCY_PER_KWH = "currencyPerKWh"


class OadrDataQualityType(Enum):
    NO_QUALITY_NO_VALUE = "No Quality - No Value"
    NO_NEW_VALUE_PREVIOUS_VALUE_USED = "No New Value - Previous Value Used"
    QUALITY_BAD_NON_SPECIFIC = "Quality Bad - Non Specific"
    QUALITY_BAD_CONFIGURATION_ERROR = "Quality Bad - Configuration Error"
    QUALITY_BAD_NOT_CONNECTED = "Quality Bad - Not Connected"
    QUALITY_BAD_DEVICE_FAILURE = "Quality Bad - Device Failure"
    QUALITY_BAD_SENSOR_FAILURE = "Quality Bad - Sensor Failure"
    QUALITY_BAD_LAST_KNOWN_VALUE = "Quality Bad - Last Known Value"
    QUALITY_BAD_COMM_FAILURE = "Quality Bad - Comm Failure"
    QUALITY_BAD_OUT_OF_SERVICE = "Quality Bad - Out of Service"
    QUALITY_UNCERTAIN_NON_SPECIFIC = "Quality Uncertain - Non Specific"
    QUALITY_UNCERTAIN_LAST_USABLE_VALUE = "Quality Uncertain - Last Usable Value"
    QUALITY_UNCERTAIN_SENSOR_NOT_ACCURATE = "Quality Uncertain - Sensor Not Accurate"
    QUALITY_UNCERTAIN_EU_UNITS_EXCEEDED = "Quality Uncertain - EU Units Exceeded"
    QUALITY_UNCERTAIN_SUB_NORMAL = "Quality Uncertain - Sub Normal"
    QUALITY_GOOD_NON_SPECIFIC = "Quality Good - Non Specific"
    QUALITY_GOOD_LOCAL_OVERRIDE = "Quality Good - Local Override"
    QUALITY_LIMIT_FIELD_NOT = "Quality Limit - Field/Not"
    QUALITY_LIMIT_FIELD_LOW = "Quality Limit - Field/Low"
    QUALITY_LIMIT_FIELD_HIGH = "Quality Limit - Field/High"
    QUALITY_LIMIT_FIELD_CONSTANT = "Quality Limit - Field/Constant"


@dataclass
class OadrHttpPullModel:
    class Meta:
        name = "oadrHttpPullModel"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrInfo:
    """
    A key value pair of service specific registration information.
    """
    class Meta:
        name = "oadrInfo"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrKey",
            "type": "Element",
            "required": True,
        }
    )
    oadr_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OadrLoadControlStateTypeType:
    class Meta:
        name = "oadrLoadControlStateTypeType"

    oadr_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrMin",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrMax",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_current: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrCurrent",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_normal: Optional[float] = field(
        default=None,
        metadata={
            "name": "oadrNormal",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


@dataclass
class OadrPendingReportsType:
    class Meta:
        name = "oadrPendingReportsType"

    report_request_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


class OadrProfileType(Enum):
    VALUE_2_0A = "2.0a"
    VALUE_2_0B = "2.0b"


@dataclass
class OadrReportOnly:
    """
    ReportOnlyDeviceFlag.
    """
    class Meta:
        name = "oadrReportOnly"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrSamplingRateType:
    """
    :ivar oadr_min_period: Minimum sampling period
    :ivar oadr_max_period: Maximum sampling period
    :ivar oadr_on_change: If true then the data will be recorded when it
        changes, but at no greater a frequency than that specified  by
        minPeriod.
    """
    class Meta:
        name = "oadrSamplingRateType"

    oadr_min_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrMinPeriod",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )
    oadr_max_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "oadrMaxPeriod",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )
    oadr_on_change: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrOnChange",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )


class OadrServiceNameType(Enum):
    EI_EVENT = "EiEvent"
    EI_OPT = "EiOpt"
    EI_REPORT = "EiReport"
    EI_REGISTER_PARTY = "EiRegisterParty"
    OADR_POLL = "OadrPoll"


@dataclass
class OadrTransportAddress:
    """Root address used to communicate with other party.

    Should include port if required
    """
    class Meta:
        name = "oadrTransportAddress"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class OadrTransportType(Enum):
    SIMPLE_HTTP = "simpleHttp"
    XMPP = "xmpp"


@dataclass
class OadrVenName:
    """VEN name.

    May be used in VTN GUI
    """
    class Meta:
        name = "oadrVenName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrXmlSignature:
    """
    Implementation supports XML signature.
    """
    class Meta:
        name = "oadrXmlSignature"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PulseFactor:
    """
    kWh per count.
    """
    class Meta:
        name = "pulseFactor"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


class TemperatureUnitType(Enum):
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"


@dataclass
class BaseUnitType(ItemBaseType):
    """
    Custom Units.
    """
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class CurrentType(ItemBaseType):
    """
    Current.
    """
    item_description: str = field(
        init=False,
        default="Current",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="A",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class FrequencyType(ItemBaseType):
    """
    Frequency.
    """
    item_description: str = field(
        init=False,
        default="Frequency",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="Hz",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class ThermType(ItemBaseType):
    """
    Therm.
    """
    item_description: str = field(
        init=False,
        default="Therm",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="thm",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class CurrencyType(ItemBaseType):
    """
    currency.

    :ivar item_description:
    :ivar item_units: ISO enumeration of currency types, such as USD
    :ivar si_scale_code:
    """
    class Meta:
        name = "currencyType"

    item_description: Optional[CurrencyItemDescriptionType] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: Optional[Iso3AlphaCurrencyCodeContentType] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class OadrCancelOptType:
    class Meta:
        name = "oadrCancelOptType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    opt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "optID",
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


@dataclass
class OadrCanceledOptType:
    class Meta:
        name = "oadrCanceledOptType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    opt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "optID",
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


@dataclass
class OadrCanceledPartyRegistrationType:
    class Meta:
        name = "oadrCanceledPartyRegistrationType"

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


@dataclass
class OadrCreatedOptType:
    class Meta:
        name = "oadrCreatedOptType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    opt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "optID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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


@dataclass
class OadrDataQuality:
    class Meta:
        name = "oadrDataQuality"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Union[OadrDataQualityType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class OadrDeviceClass(EiTargetType):
    """Device Class target - use only endDeviceAsset."""
    class Meta:
        name = "oadrDeviceClass"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDistributeEventType:
    """
    :ivar ei_response:
    :ivar request_id:
    :ivar vtn_id:
    :ivar oadr_event: An object containing a demand response event
    :ivar schema_version:
    """
    class Meta:
        name = "oadrDistributeEventType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
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
    oadr_event: List["OadrDistributeEventType.OadrEvent"] = field(
        default_factory=list,
        metadata={
            "name": "oadrEvent",
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
    class OadrEvent:
        ei_event: Optional[EiEvent] = field(
            default=None,
            metadata={
                "name": "eiEvent",
                "type": "Element",
                "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
                "required": True,
            }
        )
        oadr_response_required: Optional[ResponseRequiredType] = field(
            default=None,
            metadata={
                "name": "oadrResponseRequired",
                "type": "Element",
                "namespace": "http://openadr.org/oadr-2.0b/2012/07",
                "required": True,
            }
        )


@dataclass
class OadrGbitemBase(ItemBaseType):
    class Meta:
        name = "oadrGBItemBase"

    feed: Optional[Feed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "required": True,
        }
    )


@dataclass
class OadrGbstreamPayloadBase(StreamPayloadBaseType):
    class Meta:
        name = "oadrGBStreamPayloadBase"

    feed: Optional[Feed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "required": True,
        }
    )


@dataclass
class OadrLoadControlStateType:
    class Meta:
        name = "oadrLoadControlStateType"

    oadr_capacity: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrCapacity",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_level_offset: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrLevelOffset",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_percent_offset: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrPercentOffset",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_set_point: Optional[OadrLoadControlStateTypeType] = field(
        default=None,
        metadata={
            "name": "oadrSetPoint",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


@dataclass
class OadrPendingReports(OadrPendingReportsType):
    class Meta:
        name = "oadrPendingReports"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPollType:
    class Meta:
        name = "oadrPollType"

    ven_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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


@dataclass
class OadrProfileName:
    """
    OpenADR profile name such as 2.0a or 2.0b.
    """
    class Meta:
        name = "oadrProfileName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrProfileType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrQueryRegistrationType:
    class Meta:
        name = "oadrQueryRegistrationType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
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


@dataclass
class OadrReportPayloadType(ReportPayloadType):
    """
    Report payload for use in reports.

    :ivar oadr_data_quality: Enumerated value for the quality of this
        data item
    """
    class Meta:
        name = "oadrReportPayloadType"

    oadr_data_quality: Optional[Union[OadrDataQualityType, str]] = field(
        default=None,
        metadata={
            "name": "oadrDataQuality",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class OadrReportRequestType:
    """
    This type is used to request an EiReport.
    """
    class Meta:
        name = "oadrReportRequestType"

    report_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_specifier: Optional[ReportSpecifier] = field(
        default=None,
        metadata={
            "name": "reportSpecifier",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )


@dataclass
class OadrRequestEventType:
    class Meta:
        name = "oadrRequestEventType"

    ei_request_event: Optional[EiRequestEvent] = field(
        default=None,
        metadata={
            "name": "eiRequestEvent",
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


@dataclass
class OadrRequestReregistrationType:
    class Meta:
        name = "oadrRequestReregistrationType"

    ven_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
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


@dataclass
class OadrRequestedOadrPollFreq(DurationPropType):
    """
    The VEN shall send an oadrPoll payload to the VTN at most once for each
    duration specified by this element.
    """
    class Meta:
        name = "oadrRequestedOadrPollFreq"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrResponseRequired:
    """Controls when optIn/optOut repsonse is required.

    Can be always or never
    """
    class Meta:
        name = "oadrResponseRequired"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[ResponseRequiredType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrResponseType:
    class Meta:
        name = "oadrResponseType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
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


@dataclass
class OadrSamplingRate(OadrSamplingRateType):
    """
    Sampling rate for telemetry type data.
    """
    class Meta:
        name = "oadrSamplingRate"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrServiceName:
    class Meta:
        name = "oadrServiceName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrServiceNameType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrServiceSpecificInfo:
    """
    Service specific registration information.
    """
    class Meta:
        name = "oadrServiceSpecificInfo"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_service: List["OadrServiceSpecificInfo.OadrService"] = field(
        default_factory=list,
        metadata={
            "name": "oadrService",
            "type": "Element",
        }
    )

    @dataclass
    class OadrService:
        oadr_service_name: Optional[OadrServiceNameType] = field(
            default=None,
            metadata={
                "name": "oadrServiceName",
                "type": "Element",
                "required": True,
            }
        )
        oadr_info: List[OadrInfo] = field(
            default_factory=list,
            metadata={
                "name": "oadrInfo",
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class OadrTransportName:
    """
    OpenADR transport name such as simpleHttp or xmpp.
    """
    class Meta:
        name = "oadrTransportName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrTransportType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OadrTransports:
    """
    OpenADR transports supported by implementation.
    """
    class Meta:
        name = "oadrTransports"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_transport: List["OadrTransports.OadrTransport"] = field(
        default_factory=list,
        metadata={
            "name": "oadrTransport",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class OadrTransport:
        oadr_transport_name: Optional[OadrTransportType] = field(
            default=None,
            metadata={
                "name": "oadrTransportName",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class PulseCountType(ItemBaseType):
    """
    Pulse Count.

    :ivar item_description:
    :ivar item_units: Pulse count from meter
    :ivar pulse_factor:
    """
    class Meta:
        name = "pulseCountType"

    item_description: str = field(
        init=False,
        default="pulse count",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="count",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    pulse_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "pulseFactor",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )


@dataclass
class TemperatureType(ItemBaseType):
    """
    temperature.

    :ivar item_description:
    :ivar item_units: Temperature in Celsius or Fahrenheit
    :ivar si_scale_code:
    """
    class Meta:
        name = "temperatureType"

    item_description: str = field(
        init=False,
        default="temperature",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: Optional[TemperatureUnitType] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass
class Therm(ThermType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Currency(CurrencyType):
    class Meta:
        name = "currency"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerKw(CurrencyType):
    class Meta:
        name = "currencyPerKW"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerKwh(CurrencyType):
    class Meta:
        name = "currencyPerKWh"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerThm(CurrencyType):
    class Meta:
        name = "currencyPerThm"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Current(CurrentType):
    class Meta:
        name = "current"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CustomUnit(BaseUnitType):
    class Meta:
        name = "customUnit"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Frequency(FrequencyType):
    class Meta:
        name = "frequency"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelOpt(OadrCancelOptType):
    """
    Cancel an opt schedule.
    """
    class Meta:
        name = "oadrCancelOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelPartyRegistration(OadrCancelPartyRegistrationType):
    """
    Cancel a registration.
    """
    class Meta:
        name = "oadrCancelPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelReport(OadrCancelReportType):
    """
    Cancel a report.
    """
    class Meta:
        name = "oadrCancelReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledOpt(OadrCanceledOptType):
    """
    Acknowledge cancelation of an opt schedule.
    """
    class Meta:
        name = "oadrCanceledOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledPartyRegistration(OadrCanceledPartyRegistrationType):
    """
    Acknowledge cancelation of registration.
    """
    class Meta:
        name = "oadrCanceledPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledReportType:
    class Meta:
        name = "oadrCanceledReportType"

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


@dataclass
class OadrCreateOptType(EiOptType):
    class Meta:
        name = "oadrCreateOptType"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110/payloads",
            "required": True,
        }
    )
    qualified_event_id: Optional[QualifiedEventId] = field(
        default=None,
        metadata={
            "name": "qualifiedEventID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ei_target: Optional[EiTarget] = field(
        default=None,
        metadata={
            "name": "eiTarget",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_device_class: Optional[OadrDeviceClass] = field(
        default=None,
        metadata={
            "name": "oadrDeviceClass",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


@dataclass
class OadrCreatePartyRegistration(OadrCreatePartyRegistrationType):
    """
    Used by VEN to initiate registration with VTN.
    """
    class Meta:
        name = "oadrCreatePartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedEvent(OadrCreatedEventType):
    class Meta:
        name = "oadrCreatedEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedOpt(OadrCreatedOptType):
    """
    Acknowledge receipt of an opt schedule.
    """
    class Meta:
        name = "oadrCreatedOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


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


@dataclass
class OadrDistributeEvent(OadrDistributeEventType):
    """
    Send DR Events to a VEN.
    """
    class Meta:
        name = "oadrDistributeEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbdataDescription(OadrGbitemBase):
    class Meta:
        name = "oadrGBDataDescription"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbpayload(OadrGbstreamPayloadBase):
    class Meta:
        name = "oadrGBPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrLoadControlState(OadrLoadControlStateType):
    class Meta:
        name = "oadrLoadControlState"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPoll(OadrPollType):
    """
    Query pull VTN for payloads with new or modified information.
    """
    class Meta:
        name = "oadrPoll"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrProfiles:
    """
    OpenADR profiles supported by the implementation.
    """
    class Meta:
        name = "oadrProfiles"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_profile: List["OadrProfiles.OadrProfile"] = field(
        default_factory=list,
        metadata={
            "name": "oadrProfile",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class OadrProfile:
        oadr_profile_name: Optional[OadrProfileType] = field(
            default=None,
            metadata={
                "name": "oadrProfileName",
                "type": "Element",
                "required": True,
            }
        )
        oadr_transports: Optional[OadrTransports] = field(
            default=None,
            metadata={
                "name": "oadrTransports",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class OadrQueryRegistration(OadrQueryRegistrationType):
    """
    Query VTN for registration information without actually registering.
    """
    class Meta:
        name = "oadrQueryRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportPayload(OadrReportPayloadType):
    """
    Data point values for reports.
    """
    class Meta:
        name = "oadrReportPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportRequest(OadrReportRequestType):
    class Meta:
        name = "oadrReportRequest"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestEvent(OadrRequestEventType):
    class Meta:
        name = "oadrRequestEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestReregistration(OadrRequestReregistrationType):
    """
    Used by VTN to request that the VEN reregister.
    """
    class Meta:
        name = "oadrRequestReregistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrResponse(OadrResponseType):
    class Meta:
        name = "oadrResponse"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class PulseCount(PulseCountType):
    class Meta:
        name = "pulseCount"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Temperature(TemperatureType):
    class Meta:
        name = "temperature"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledReport(OadrCanceledReportType):
    class Meta:
        name = "oadrCanceledReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreateOpt(OadrCreateOptType):
    """
    Create an optIn or optOut schedule.
    """
    class Meta:
        name = "oadrCreateOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


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


@dataclass
class OadrCreatedReport(OadrCreatedReportType):
    """
    Acknowledge the request for report was received.
    """
    class Meta:
        name = "oadrCreatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayloadResourceStatusType(PayloadBaseType):
    """
    This is the payload for reports that require a status.

    :ivar oadr_online: If true then resource/asset is online, if false
        then offline.
    :ivar oadr_manual_override: If true then the control of the load has
        been manually overridden
    :ivar oadr_load_control_state:
    """
    class Meta:
        name = "oadrPayloadResourceStatusType"

    oadr_online: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrOnline",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_manual_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "oadrManualOverride",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    oadr_load_control_state: Optional[OadrLoadControlState] = field(
        default=None,
        metadata={
            "name": "oadrLoadControlState",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


@dataclass
class OadrRegisteredReportType:
    class Meta:
        name = "oadrRegisteredReportType"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_report_request: List[OadrReportRequest] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportRequest",
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


@dataclass
class OadrReportDescriptionType:
    """
    Describes the subject and attributes of a report.
    """
    class Meta:
        name = "oadrReportDescriptionType"

    r_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "rID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_subject: Optional[ReportSubject] = field(
        default=None,
        metadata={
            "name": "reportSubject",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    report_data_source: Optional[ReportDataSource] = field(
        default=None,
        metadata={
            "name": "reportDataSource",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    report_type: Optional[Union[ReportEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "reportType",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"x-\S.*",
        }
    )
    oadr_gbdata_description: Optional[OadrGbdataDescription] = field(
        default=None,
        metadata={
            "name": "oadrGBDataDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    pulse_count: Optional[PulseCount] = field(
        default=None,
        metadata={
            "name": "pulseCount",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    therm: Optional[Therm] = field(
        default=None,
        metadata={
            "name": "Therm",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    frequency: Optional[Frequency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_thm: Optional[CurrencyPerThm] = field(
        default=None,
        metadata={
            "name": "currencyPerThm",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_kw: Optional[CurrencyPerKw] = field(
        default=None,
        metadata={
            "name": "currencyPerKW",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_kwh: Optional[CurrencyPerKwh] = field(
        default=None,
        metadata={
            "name": "currencyPerKWh",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    current: Optional[Current] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    custom_unit: Optional[CustomUnit] = field(
        default=None,
        metadata={
            "name": "customUnit",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    power_real: Optional[PowerReal] = field(
        default=None,
        metadata={
            "name": "powerReal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_reactive: Optional[PowerReactive] = field(
        default=None,
        metadata={
            "name": "powerReactive",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_apparent: Optional[PowerApparent] = field(
        default=None,
        metadata={
            "name": "powerApparent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_item: Optional[PowerItem] = field(
        default=None,
        metadata={
            "name": "powerItem",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_real: Optional[EnergyReal] = field(
        default=None,
        metadata={
            "name": "energyReal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_reactive: Optional[EnergyReactive] = field(
        default=None,
        metadata={
            "name": "energyReactive",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_apparent: Optional[EnergyApparent] = field(
        default=None,
        metadata={
            "name": "energyApparent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_item: Optional[EnergyItem] = field(
        default=None,
        metadata={
            "name": "energyItem",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    voltage: Optional[Voltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    reading_type: Optional[Union[ReadingTypeEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "readingType",
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
    oadr_sampling_rate: Optional[OadrSamplingRate] = field(
        default=None,
        metadata={
            "name": "oadrSamplingRate",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


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


@dataclass
class OadrCreateReport(OadrCreateReportType):
    """
    Request report from other party.
    """
    class Meta:
        name = "oadrCreateReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedPartyRegistration(OadrCreatedPartyRegistrationType):
    """
    Acknowledge receipt of VEN registration, provide VTN registration info.
    """
    class Meta:
        name = "oadrCreatedPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPayloadResourceStatus(OadrPayloadResourceStatusType):
    """
    Current resource status information.
    """
    class Meta:
        name = "oadrPayloadResourceStatus"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRegisteredReport(OadrRegisteredReportType):
    """
    Acknowledge registration of Metadata report by other party.
    """
    class Meta:
        name = "oadrRegisteredReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportDescription(OadrReportDescriptionType):
    class Meta:
        name = "oadrReportDescription"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdatedReport(OadrUpdatedReportType):
    """
    Acknowledge receipt of a report.
    """
    class Meta:
        name = "oadrUpdatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrReportType(StreamBaseType):
    """eiReport is a Stream of [measurements] recorded over time and delivered
    to the requestor periodically.

    The readings may be actual, computed, summed if derived in some
    other manner.

    :ivar ei_report_id: reference ID to this report.
    :ivar oadr_report_description: Define data points the implementation
        is capable of reporting on. Only used in Metadata report
    :ivar report_request_id: Reference to the oadrCreateReport request
        that defined this report.
    :ivar report_specifier_id: Reference to Metadata report from which
        this report was derived.
    :ivar report_name: Name possibly for use in a user interface.
    :ivar created_date_time:
    """
    class Meta:
        name = "oadrReportType"

    ei_report_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "eiReportID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    oadr_report_description: List[OadrReportDescription] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    report_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportRequestID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_specifier_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportSpecifierID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_name: Optional[Union[ReportNameEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "reportName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"x-\S.*",
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


@dataclass
class OadrReport(OadrReportType):
    class Meta:
        name = "oadrReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


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


@dataclass
class OadrUpdateReportType:
    class Meta:
        name = "oadrUpdateReportType"

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
class OadrRegisterReport(OadrRegisterReportType):
    """
    Register Metadata report settings with other party.
    """
    class Meta:
        name = "oadrRegisterReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdateReport(OadrUpdateReportType):
    """
    Send a previously requested report.
    """
    class Meta:
        name = "oadrUpdateReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrSignedObject:
    class Meta:
        name = "oadrSignedObject"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_distribute_event: Optional[OadrDistributeEvent] = field(
        default=None,
        metadata={
            "name": "oadrDistributeEvent",
            "type": "Element",
        }
    )
    oadr_created_event: Optional[OadrCreatedEvent] = field(
        default=None,
        metadata={
            "name": "oadrCreatedEvent",
            "type": "Element",
        }
    )
    oadr_request_event: Optional[OadrRequestEvent] = field(
        default=None,
        metadata={
            "name": "oadrRequestEvent",
            "type": "Element",
        }
    )
    oadr_response: Optional[OadrResponse] = field(
        default=None,
        metadata={
            "name": "oadrResponse",
            "type": "Element",
        }
    )
    oadr_cancel_opt: Optional[OadrCancelOpt] = field(
        default=None,
        metadata={
            "name": "oadrCancelOpt",
            "type": "Element",
        }
    )
    oadr_canceled_opt: Optional[OadrCanceledOpt] = field(
        default=None,
        metadata={
            "name": "oadrCanceledOpt",
            "type": "Element",
        }
    )
    oadr_create_opt: Optional[OadrCreateOpt] = field(
        default=None,
        metadata={
            "name": "oadrCreateOpt",
            "type": "Element",
        }
    )
    oadr_created_opt: Optional[OadrCreatedOpt] = field(
        default=None,
        metadata={
            "name": "oadrCreatedOpt",
            "type": "Element",
        }
    )
    oadr_cancel_report: Optional[OadrCancelReport] = field(
        default=None,
        metadata={
            "name": "oadrCancelReport",
            "type": "Element",
        }
    )
    oadr_canceled_report: Optional[OadrCanceledReport] = field(
        default=None,
        metadata={
            "name": "oadrCanceledReport",
            "type": "Element",
        }
    )
    oadr_create_report: Optional[OadrCreateReport] = field(
        default=None,
        metadata={
            "name": "oadrCreateReport",
            "type": "Element",
        }
    )
    oadr_created_report: Optional[OadrCreatedReport] = field(
        default=None,
        metadata={
            "name": "oadrCreatedReport",
            "type": "Element",
        }
    )
    oadr_register_report: Optional[OadrRegisterReport] = field(
        default=None,
        metadata={
            "name": "oadrRegisterReport",
            "type": "Element",
        }
    )
    oadr_registered_report: Optional[OadrRegisteredReport] = field(
        default=None,
        metadata={
            "name": "oadrRegisteredReport",
            "type": "Element",
        }
    )
    oadr_update_report: Optional[OadrUpdateReport] = field(
        default=None,
        metadata={
            "name": "oadrUpdateReport",
            "type": "Element",
        }
    )
    oadr_updated_report: Optional[OadrUpdatedReport] = field(
        default=None,
        metadata={
            "name": "oadrUpdatedReport",
            "type": "Element",
        }
    )
    oadr_cancel_party_registration: Optional[OadrCancelPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCancelPartyRegistration",
            "type": "Element",
        }
    )
    oadr_canceled_party_registration: Optional[OadrCanceledPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCanceledPartyRegistration",
            "type": "Element",
        }
    )
    oadr_create_party_registration: Optional[OadrCreatePartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCreatePartyRegistration",
            "type": "Element",
        }
    )
    oadr_created_party_registration: Optional[OadrCreatedPartyRegistration] = field(
        default=None,
        metadata={
            "name": "oadrCreatedPartyRegistration",
            "type": "Element",
        }
    )
    oadr_request_reregistration: Optional[OadrRequestReregistration] = field(
        default=None,
        metadata={
            "name": "oadrRequestReregistration",
            "type": "Element",
        }
    )
    oadr_query_registration: Optional[OadrQueryRegistration] = field(
        default=None,
        metadata={
            "name": "oadrQueryRegistration",
            "type": "Element",
        }
    )
    oadr_poll: Optional[OadrPoll] = field(
        default=None,
        metadata={
            "name": "oadrPoll",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )


@dataclass
class OadrPayload:
    class Meta:
        name = "oadrPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    oadr_signed_object: Optional[OadrSignedObject] = field(
        default=None,
        metadata={
            "name": "oadrSignedObject",
            "type": "Element",
            "required": True,
        }
    )
