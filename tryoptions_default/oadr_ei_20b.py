from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from tryoptions_default.oadr_20b import (
    Therm,
    Currency,
    CurrencyPerKw,
    CurrencyPerKwh,
    CurrencyPerThm,
    Current,
    CustomUnit,
    Frequency,
    OadrGbdataDescription,
    OadrGbpayload,
    OadrPayloadResourceStatus,
    OadrReportPayload,
    PulseCount,
    Temperature,
)
from tryoptions_default.oadr_emix_20b import ServiceArea
from tryoptions_default.oadr_power_20b import (
    AggregatedPnode,
    EndDeviceAsset,
    EnergyApparent,
    EnergyItem,
    EnergyReactive,
    EnergyReal,
    MeterAsset,
    Pnode,
    PowerApparent,
    PowerItem,
    PowerReactive,
    PowerReal,
    ServiceDeliveryPoint,
    ServiceLocation,
    TransportInterface,
    Voltage,
)
from tryoptions_default.oadr_strm_20b import (
    StreamPayloadBaseType,
    Intervals,
)
from tryoptions_default.oadr_xcal_20b import (
    DurationPropType,
    WsCalendarIntervalType,
    Components,
    Dtstart,
    Duration,
    Granularity,
    Properties,
    Uid,
    Vavailability,
)

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiResponseType:
    response_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "responseCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"[0-9][0-9][0-9]",
        }
    )
    response_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "responseDescription",
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


class EventStatusEnumeratedType(Enum):
    """
    :cvar NONE: No event pending
    :cvar FAR: Event pending in the far future. The exact definition of
        how far in the future this refers is dependent upon the market
        context, but typically means the next day.
    :cvar NEAR: Event pending in the near future. The exact definition
        of how near in the future the pending event is active is
        dependent on the market context.
    :cvar ACTIVE: The event has been initiated and is currently active.
    :cvar COMPLETED: The event has completed.
    :cvar CANCELLED: The event has been canceled.
    """
    NONE = "none"
    FAR = "far"
    NEAR = "near"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class OptReasonEnumeratedType(Enum):
    """
    Enumerated reasons for opting.
    """
    ECONOMIC = "economic"
    EMERGENCY = "emergency"
    MUST_RUN = "mustRun"
    NOT_PARTICIPATING = "notParticipating"
    OUTAGE_RUN_STATUS = "outageRunStatus"
    OVERRIDE_STATUS = "overrideStatus"
    PARTICIPATING = "participating"
    X_SCHEDULE = "x-schedule"


class OptTypeType(Enum):
    OPT_IN = "optIn"
    OPT_OUT = "optOut"


@dataclass
class PayloadBaseType:
    """
    Base for information in signal / baseline / report payloads.
    """


@dataclass
class QualifiedEventIdtype:
    """
    Fully qualified event ID includes the eventID and the modificationNumber.
    """
    class Meta:
        name = "QualifiedEventIDType"

    event_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    modification_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "modificationNumber",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )


class ReadingTypeEnumeratedType(Enum):
    """
    :cvar DIRECT_READ: Reading is read from a device that increases
        monotonically, and usage must be computed from pairs of start
        and stop readings.
    :cvar NET: Meter or [resource] prepares its own calculation of total
        use over time.
    :cvar ALLOCATED: Meter covers several [resources] and usage is
        inferred through some sort of pro data computation.
    :cvar ESTIMATED: Used when a reading is absent in a series in which
        most readings are present.
    :cvar SUMMED: Several meters together provide the reading for this
        [resource]. This is specifically a different than aggregated,
        which refers to multiple [resources] in the same payload. See
        also Hybrid.
    :cvar DERIVED: Usage is inferred through knowledge of run-time,
        normal operation, etc.
    :cvar MEAN: Reading is the mean value over the period indicated in
        Granularity
    :cvar PEAK: Reading is Peak (highest) value over the period
        indicated in granularity. For some measurements, it may make
        more sense as the lowest value. May not be consistent with
        aggregate readings. Only valid for flow-rate Item Bases, i.e.,
        Power not Energy.
    :cvar HYBRID: If aggregated, refers to different reading types in
        the aggregate number.
    :cvar CONTRACT: Indicates reading is pro forma, i.e., is reported at
        agreed upon rates
    :cvar PROJECTED: Indicates reading is in the future, and has not yet
        been measured.
    :cvar X_RMS: Root Mean Square
    :cvar X_NOT_APPLICABLE: Not Applicable
    """
    DIRECT_READ = "Direct Read"
    NET = "Net"
    ALLOCATED = "Allocated"
    ESTIMATED = "Estimated"
    SUMMED = "Summed"
    DERIVED = "Derived"
    MEAN = "Mean"
    PEAK = "Peak"
    HYBRID = "Hybrid"
    CONTRACT = "Contract"
    PROJECTED = "Projected"
    X_RMS = "x-RMS"
    X_NOT_APPLICABLE = "x-notApplicable"


class ReportEnumeratedType(Enum):
    """
    Enumerated report types.

    :cvar READING: Report indicates a reading, as from a meter. Readings
        are moments in time-changes over time can be computed from the
        difference between successive readings. Payload type is float
    :cvar USAGE: Report indicates an amount of units (denominated in
        ItemBase or in the EMIX Product) over a period. Payload type is
        Quantity. A typical ItemBase is Real Energy.
    :cvar DEMAND: Report indicates an amount of units (denominated in
        ItemBase or in the EMIX Product). Payload type is Quantity. A
        typical ItemBase is Real Power.
    :cvar SET_POINT: Report indicates the amount (denominated in
        ItemBase or in the EMIX Product) currently set. May be a
        confirmation/return of the setpoint control value sent from the
        VTN. Payload type is Quantity. A typical ItemBase is Real Power.
    :cvar DELTA_USAGE: Change in usage as compared to the baseline. See
        usage for more information
    :cvar DELTA_SET_POINT: Changes in setpoint from previous schedule.
    :cvar DELTA_DEMAND: Change in demand as compared to the baseline.
        See demand for more information
    :cvar BASELINE: Can be demand or usage, as indicated by ItemBase.
        Indicates what [measurement] would be if not for the event or
        regulation. Report is of the format Baseline.
    :cvar DEVIATION: Difference between some instruction and actual
        state.
    :cvar AVG_USAGE: Average usage over the duration indicated by the
        Granularity. See usage for more information.
    :cvar AVG_DEMAND: Average usage over the duration indicated by the
        Granularity. See demand for more information.
    :cvar OPERATING_STATE: Generalized state of a resource such as
        on/off, occupancy of building, etc. No ItemBase is relevant.
        Requires an Application Specific Payload Extension.
    :cvar UP_REGULATION_CAPACITY_AVAILABLE: Up Regulation capacity
        available for dispatch, expressed in EMIX Real Power. Payload is
        always expressed as positive Quantity.
    :cvar DOWN_REGULATION_CAPACITY_AVAILABLE: Down Regulation capacity
        available for dispatch, expressed in EMIX Real Power. Payload is
        always expressed as positive Quantity.
    :cvar REGULATION_SETPOINT: Regulation setpoint as instructed as part
        of regulation services
    :cvar STORED_ENERGY: Stored Energy is expressed as Real Energy and
        Payload is expressed as a Quantity.
    :cvar TARGET_ENERGY_STORAGE: Target Energy is expressed as Real
        Energy and Payload is expressed as a Quantity.
    :cvar AVAILABLE_ENERGY_STORAGE: Capacity available for further
        energy storage, perhaps to get to Target Energy Storage
    :cvar PRICE: Price per ItemBase at each Interval
    :cvar LEVEL: Simple level from market at each Interval. Itembase is
        not relevant.
    :cvar POWER_FACTOR: Power factor for the resource.
    :cvar PERCENT_USAGE: Percentage of usage.
    :cvar PERCENT_DEMAND: Percentage of demand
    :cvar X_RESOURCE_STATUS: Percentage of demand
    """
    READING = "reading"
    USAGE = "usage"
    DEMAND = "demand"
    SET_POINT = "setPoint"
    DELTA_USAGE = "deltaUsage"
    DELTA_SET_POINT = "deltaSetPoint"
    DELTA_DEMAND = "deltaDemand"
    BASELINE = "baseline"
    DEVIATION = "deviation"
    AVG_USAGE = "avgUsage"
    AVG_DEMAND = "avgDemand"
    OPERATING_STATE = "operatingState"
    UP_REGULATION_CAPACITY_AVAILABLE = "upRegulationCapacityAvailable"
    DOWN_REGULATION_CAPACITY_AVAILABLE = "downRegulationCapacityAvailable"
    REGULATION_SETPOINT = "regulationSetpoint"
    STORED_ENERGY = "storedEnergy"
    TARGET_ENERGY_STORAGE = "targetEnergyStorage"
    AVAILABLE_ENERGY_STORAGE = "availableEnergyStorage"
    PRICE = "price"
    LEVEL = "level"
    POWER_FACTOR = "powerFactor"
    PERCENT_USAGE = "percentUsage"
    PERCENT_DEMAND = "percentDemand"
    X_RESOURCE_STATUS = "x-resourceStatus"


class SignalNameEnumeratedType(Enum):
    """
    :cvar SIMPLE: Simple levels (OpenADR 2.0a compliant)
    :cvar SIMPLE_1: depreciated - for backwards compatibility with A
        profile
    :cvar ELECTRICITY_PRICE: This is the cost of electricity
    :cvar ENERGY_PRICE: This is the cost of energy
    :cvar DEMAND_CHARGE: This is the demand charge
    :cvar BID_PRICE: This is the price that was bid by the resource
    :cvar BID_LOAD: This is the amount of load that was bid by a
        resource into a program
    :cvar BID_ENERGY: This is the amount of energy from a resource that
        was bid into a program
    :cvar CHARGE_STATE: State of energy storage resource
    :cvar LOAD_DISPATCH: This is used to dispatch load
    :cvar LOAD_CONTROL: Set load output to relative values
    """
    SIMPLE = "SIMPLE"
    SIMPLE_1 = "simple"
    ELECTRICITY_PRICE = "ELECTRICITY_PRICE"
    ENERGY_PRICE = "ENERGY_PRICE"
    DEMAND_CHARGE = "DEMAND_CHARGE"
    BID_PRICE = "BID_PRICE"
    BID_LOAD = "BID_LOAD"
    BID_ENERGY = "BID_ENERGY"
    CHARGE_STATE = "CHARGE_STATE"
    LOAD_DISPATCH = "LOAD_DISPATCH"
    LOAD_CONTROL = "LOAD_CONTROL"


class SignalTypeEnumeratedType(Enum):
    """
    SignalTypeEnumerated lists the pre-defined types used to specify the
    payload types and conformance in a stream.

    :cvar DELTA: Signal indicates the amount to change from what one
        would have used without the signal.
    :cvar LEVEL: Signal indicates a program level.
    :cvar MULTIPLIER: Signal indicates a multiplier applied to the
        current rate of  delivery or usage from what one would have used
        without the signal.
    :cvar PRICE: Signal indicates the price.
    :cvar PRICE_MULTIPLIER: Signal indicates the price multiplier.
        Extended price is the computed price value multiplied by the
        number of units.
    :cvar PRICE_RELATIVE: Signal indicates the relative price.
    :cvar SETPOINT: Signal indicates a target amount of units.
    :cvar X_LOAD_CONTROL_CAPACITY: This is an instruction for the load
        controller to operate at a level that is some percentage of its
        maximum load consumption capacity. This can be mapped to
        specific load controllers to do things like duty cycling. Note
        that 1.0 refers to 100% consumption. In the case of simple
        ON/OFF type devices then 0 = OFF and 1 = ON.
    :cvar X_LOAD_CONTROL_LEVEL_OFFSET: Discrete integer levels that are
        relative to normal operations where 0 is normal operations.
    :cvar X_LOAD_CONTROL_PERCENT_OFFSET: Percentage change from normal
        load control operations.
    :cvar X_LOAD_CONTROL_SETPOINT: Load controller set points.
    """
    DELTA = "delta"
    LEVEL = "level"
    MULTIPLIER = "multiplier"
    PRICE = "price"
    PRICE_MULTIPLIER = "priceMultiplier"
    PRICE_RELATIVE = "priceRelative"
    SETPOINT = "setpoint"
    X_LOAD_CONTROL_CAPACITY = "x-loadControlCapacity"
    X_LOAD_CONTROL_LEVEL_OFFSET = "x-loadControlLevelOffset"
    X_LOAD_CONTROL_PERCENT_OFFSET = "x-loadControlPercentOffset"
    X_LOAD_CONTROL_SETPOINT = "x-loadControlSetpoint"


@dataclass
class Accuracy:
    class Meta:
        name = "accuracy"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Confidence:
    class Meta:
        name = "confidence"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )


@dataclass
class CreatedDateTime:
    """
    The dateTime the payload was created.
    """
    class Meta:
        name = "createdDateTime"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class EiReportId:
    """
    Reference ID for a report.
    """
    class Meta:
        name = "eiReportID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class EventId:
    """
    An ID value that identifies a specific DR event instance.
    """
    class Meta:
        name = "eventID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class GroupId:
    class Meta:
        name = "groupID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class GroupName:
    class Meta:
        name = "groupName"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ModificationNumber:
    """
    Incremented each time an event is modified.
    """
    class Meta:
        name = "modificationNumber"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class NumDataSources:
    class Meta:
        name = "numDataSources"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OptId:
    """
    Identifier for an opt interaction.
    """
    class Meta:
        name = "optID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class PartyId:
    class Meta:
        name = "partyID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class RId:
    """
    ReferenceID for this data point.
    """
    class Meta:
        name = "rID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class RefId:
    """Reference ID for a particular instance, transmittal, or artifact.

    Note: not the same as the native ID of the object being transmitted or shared.
    """
    class Meta:
        name = "refID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class RegistrationId:
    """Identifier for Registration transaction.

    Not included in response to query registration unless already
    registered
    """
    class Meta:
        name = "registrationID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


class ReportNameEnumeratedType(Enum):
    METADATA_HISTORY_USAGE = "METADATA_HISTORY_USAGE"
    HISTORY_USAGE = "HISTORY_USAGE"
    METADATA_HISTORY_GREENBUTTON = "METADATA_HISTORY_GREENBUTTON"
    HISTORY_GREENBUTTON = "HISTORY_GREENBUTTON"
    METADATA_TELEMETRY_USAGE = "METADATA_TELEMETRY_USAGE"
    TELEMETRY_USAGE = "TELEMETRY_USAGE"
    METADATA_TELEMETRY_STATUS = "METADATA_TELEMETRY_STATUS"
    TELEMETRY_STATUS = "TELEMETRY_STATUS"


@dataclass
class ReportRequestId:
    """
    Identifier for a particular report request.
    """
    class Meta:
        name = "reportRequestID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ReportSpecifierId:
    """
    Identifier for a particular Metadata report specification.
    """
    class Meta:
        name = "reportSpecifierID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ResourceId:
    class Meta:
        name = "resourceID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ResponseCode:
    """
    A 3 digit response code.
    """
    class Meta:
        name = "responseCode"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9][0-9][0-9]",
        }
    )


@dataclass
class ResponseDescription:
    """
    Narrative description of response status.
    """
    class Meta:
        name = "responseDescription"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class SchemaVersionEnumeratedType(Enum):
    VALUE_2_0A = "2.0a"
    VALUE_2_0B = "2.0b"


@dataclass
class StatusDateTime:
    """
    Date and time this artifact references.
    """
    class Meta:
        name = "statusDateTime"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class VenId:
    class Meta:
        name = "venID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class VtnId:
    class Meta:
        name = "vtnID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ArrayofResponses:
    """Collection of Responses.

    When a service operation regards multiple referenceable items, each
    referenced item may have its own response. Always accompanied by an
    overall Response Type.
    """
    response: List[EiResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


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


@dataclass
class EiTargetType:
    aggregated_pnode: List[AggregatedPnode] = field(
        default_factory=list,
        metadata={
            "name": "aggregatedPnode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    end_device_asset: List[EndDeviceAsset] = field(
        default_factory=list,
        metadata={
            "name": "endDeviceAsset",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    meter_asset: List[MeterAsset] = field(
        default_factory=list,
        metadata={
            "name": "meterAsset",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    pnode: List[Pnode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    service_area: List[ServiceArea] = field(
        default_factory=list,
        metadata={
            "name": "serviceArea",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06",
        }
    )
    service_delivery_point: List[ServiceDeliveryPoint] = field(
        default_factory=list,
        metadata={
            "name": "serviceDeliveryPoint",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    service_location: List[ServiceLocation] = field(
        default_factory=list,
        metadata={
            "name": "serviceLocation",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    transport_interface: List[TransportInterface] = field(
        default_factory=list,
        metadata={
            "name": "transportInterface",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    group_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    group_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "resourceID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ven_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    party_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "partyID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class PayloadFloatType(PayloadBaseType):
    """
    This is the payload for signals that require a quantity.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )


@dataclass
class SignalNameEnumerated:
    class Meta:
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[SignalNameEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SpecifierPayloadType:
    """
    Payload for use in Report Specifiers.
    """
    r_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "rID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
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


@dataclass
class EiActivePeriodType:
    class Meta:
        name = "eiActivePeriodType"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    components: Optional[Components] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "nillable": True,
        }
    )


@dataclass
class EiEventBaselineType:
    """
    :ivar dtstart:
    :ivar duration:
    :ivar intervals:
    :ivar baseline_id: Unique ID for a specific baseline
    :ivar resource_id:
    :ivar baseline_name: Descriptive name for baseline
    :ivar oadr_gbdata_description:
    :ivar pulse_count:
    :ivar temperature:
    :ivar therm:
    :ivar frequency:
    :ivar currency_per_thm:
    :ivar currency_per_kw:
    :ivar currency_per_kwh:
    :ivar currency:
    :ivar current:
    :ivar custom_unit:
    :ivar power_real:
    :ivar power_reactive:
    :ivar power_apparent:
    :ivar power_item:
    :ivar energy_real:
    :ivar energy_reactive:
    :ivar energy_apparent:
    :ivar energy_item:
    :ivar voltage:
    """
    class Meta:
        name = "eiEventBaselineType"

    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
            "required": True,
        }
    )
    baseline_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "baselineID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "resourceID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    baseline_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "baselineName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
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


@dataclass
class EiResponse(EiResponseType):
    """
    Indicate whether received payload is acceptable.
    """
    class Meta:
        name = "eiResponse"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventDescriptorType:
    """
    :ivar event_id:
    :ivar modification_number:
    :ivar modification_date_time: When an event is modified
    :ivar modification_reason: Why an event was modified
    :ivar priority: The priority of the event in relation to other
        events (The lower the number higher the priority. A value of
        zero (0) indicates no priority, which is the lowest priority by
        default).
    :ivar ei_market_context:
    :ivar created_date_time:
    :ivar event_status: An indication of the event state: far, near,
        active, canceled, completed
    :ivar test_event: Anything other than false indicates a test event
    :ivar vtn_comment: Any text
    """
    class Meta:
        name = "eventDescriptorType"

    event_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "eventID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    modification_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "modificationNumber",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    modification_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "modificationDateTime",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )
    modification_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "modificationReason",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ei_market_context: Optional["EventDescriptorType.EiMarketContext"] = field(
        default=None,
        metadata={
            "name": "eiMarketContext",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
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
    event_status: Optional[EventStatusEnumeratedType] = field(
        default=None,
        metadata={
            "name": "eventStatus",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    test_event: Optional[str] = field(
        default=None,
        metadata={
            "name": "testEvent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    vtn_comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "vtnComment",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )

    @dataclass
    class EiMarketContext:
        market_context: Optional[str] = field(
            default=None,
            metadata={
                "name": "marketContext",
                "type": "Element",
                "namespace": "http://docs.oasis-open.org/ns/emix/2011/06",
                "required": True,
            }
        )


@dataclass
class EventStatus:
    class Meta:
        name = "eventStatus"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[EventStatusEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OptReason:
    """
    Enumerated value for the opt reason such as x-schedule.
    """
    class Meta:
        name = "optReason"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[OptReasonEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class OptReasonEnumerated:
    class Meta:
        name = "optReasonEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[OptReasonEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OptType:
    """
    optIn or optOut of an event.
    """
    class Meta:
        name = "optType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[OptTypeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class QualifiedEventId(QualifiedEventIdtype):
    class Meta:
        name = "qualifiedEventID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReadingType:
    """
    Metadata about the Readings, such as mean or derived.
    """
    class Meta:
        name = "readingType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReadingTypeEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class ReadingTypeEnumerated:
    class Meta:
        name = "readingTypeEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[ReadingTypeEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReportEnumerated:
    class Meta:
        name = "reportEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[ReportEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReportName:
    """
    Optional name for a report.
    """
    class Meta:
        name = "reportName"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReportNameEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class ReportType:
    class Meta:
        name = "reportType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[ReportEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class SignalName:
    class Meta:
        name = "signalName"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[SignalNameEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )


@dataclass
class SignalType:
    """
    An enumerated value describing the type of signal such as level or price.
    """
    class Meta:
        name = "signalType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[SignalTypeEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class XEiNotification(DurationPropType):
    """
    The VEN should receive the DR event payload prior to dtstart minus this
    duration.
    """
    class Meta:
        name = "x-eiNotification"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class XEiRampUp(DurationPropType):
    """
    A duration before or after the event start time during which load shed
    should transit.
    """
    class Meta:
        name = "x-eiRampUp"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class XEiRecovery(DurationPropType):
    """
    A duration before or after the event end time during which load shed should
    transit.
    """
    class Meta:
        name = "x-eiRecovery"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiActivePeriod(EiActivePeriodType):
    """
    Time frames relevant to the overall event.
    """
    class Meta:
        name = "eiActivePeriod"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventBaseline(EiEventBaselineType):
    """
    B profile.
    """
    class Meta:
        name = "eiEventBaseline"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiTarget(EiTargetType):
    """Identifies the resources associated with the logical VEN interface.

    For events, the values specified are the target for the event
    """
    class Meta:
        name = "eiTarget"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventDescriptor(EventDescriptorType):
    """
    Information about the event.
    """
    class Meta:
        name = "eventDescriptor"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EventResponses:
    """
    optIn or optOut responses for received events.
    """
    class Meta:
        name = "eventResponses"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    event_response: List["EventResponses.EventResponse"] = field(
        default_factory=list,
        metadata={
            "name": "eventResponse",
            "type": "Element",
        }
    )

    @dataclass
    class EventResponse:
        response_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "responseCode",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9][0-9][0-9]",
            }
        )
        response_description: Optional[str] = field(
            default=None,
            metadata={
                "name": "responseDescription",
                "type": "Element",
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
        qualified_event_id: Optional[QualifiedEventId] = field(
            default=None,
            metadata={
                "name": "qualifiedEventID",
                "type": "Element",
                "required": True,
            }
        )
        opt_type: Optional[OptTypeType] = field(
            default=None,
            metadata={
                "name": "optType",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class PayloadFloat(PayloadFloatType):
    """
    Data point value for event signals or for reporting  current or historical
    values.
    """
    class Meta:
        name = "payloadFloat"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportDataSource(EiTargetType):
    """Sources for data in this report.

    Examples include meters or submeters. For example, if a meter is
    capable of providing two different types of measurements, then each
    measurement stream would be separately identified.
    """
    class Meta:
        name = "reportDataSource"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportSubject(EiTargetType):
    """Device Class target - use only endDeviceAsset."""
    class Meta:
        name = "reportSubject"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Responses(ArrayofResponses):
    class Meta:
        name = "responses"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SpecifierPayload(SpecifierPayloadType):
    class Meta:
        name = "specifierPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportPayloadType(StreamPayloadBaseType):
    """
    Report Payload for use in Reports, snaps, and projections.

    :ivar r_id: A reference to a metadata data point description
    :ivar confidence: Likely variability of prediction: 0-100
    :ivar accuracy: Accuracy in same units as interval payload value
    :ivar oadr_payload_resource_status:
    :ivar payload_float:
    """
    r_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "rID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    confidence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_inclusive": 0,
            "max_inclusive": 100,
        }
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    oadr_payload_resource_status: Optional[OadrPayloadResourceStatus] = field(
        default=None,
        metadata={
            "name": "oadrPayloadResourceStatus",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class ReportSpecifierType:
    """
    Parameters that define the content of a Report Stream.

    :ivar report_specifier_id:
    :ivar granularity: How frequently the [measurement] is to be
        recorded.
    :ivar report_back_duration: Report back with the Report-To-Date for
        each passing of this Duration.
    :ivar report_interval: This is the overall period of reporting.
    :ivar specifier_payload:
    """
    report_specifier_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "reportSpecifierID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    granularity: Optional[Granularity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    report_back_duration: Optional[DurationPropType] = field(
        default=None,
        metadata={
            "name": "reportBackDuration",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    report_interval: Optional[WsCalendarIntervalType] = field(
        default=None,
        metadata={
            "name": "reportInterval",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    specifier_payload: List[SpecifierPayload] = field(
        default_factory=list,
        metadata={
            "name": "specifierPayload",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )


@dataclass
class CurrentValueType:
    class Meta:
        name = "currentValueType"

    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class SignalPayloadType(StreamPayloadBaseType):
    class Meta:
        name = "signalPayloadType"

    oadr_payload_resource_status: Optional[OadrPayloadResourceStatus] = field(
        default=None,
        metadata={
            "name": "oadrPayloadResourceStatus",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class CurrentValue(CurrentValueType):
    """
    The payloadFloat value of the event interval currently executing.
    """
    class Meta:
        name = "currentValue"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportSpecifier(ReportSpecifierType):
    """
    Specify data points desired in a particular report instance.
    """
    class Meta:
        name = "reportSpecifier"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalPayload(SignalPayloadType):
    """
    Signal values for events and baselines.
    """
    class Meta:
        name = "signalPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class IntervalType:
    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    uid: Optional[Uid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )
    oadr_report_payload: List[OadrReportPayload] = field(
        default_factory=list,
        metadata={
            "name": "oadrReportPayload",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    oadr_gbpayload: List[OadrGbpayload] = field(
        default_factory=list,
        metadata={
            "name": "oadrGBPayload",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    signal_payload: List[SignalPayload] = field(
        default_factory=list,
        metadata={
            "name": "signalPayload",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class EiEventSignalType:
    """
    :ivar intervals:
    :ivar ei_target: Optionally identifies the device class associated
        with the signal. Only the endDeviceAsset subelement is used
    :ivar signal_name: Descriptive name for signal.
    :ivar signal_type:
    :ivar signal_id: unique Identifier for a specific event signal
    :ivar oadr_gbdata_description:
    :ivar pulse_count:
    :ivar temperature:
    :ivar therm:
    :ivar frequency:
    :ivar currency_per_thm:
    :ivar currency_per_kw:
    :ivar currency_per_kwh:
    :ivar currency:
    :ivar current:
    :ivar custom_unit:
    :ivar power_real:
    :ivar power_reactive:
    :ivar power_apparent:
    :ivar power_item:
    :ivar energy_real:
    :ivar energy_reactive:
    :ivar energy_apparent:
    :ivar energy_item:
    :ivar voltage:
    :ivar current_value:
    """
    class Meta:
        name = "eiEventSignalType"

    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
            "required": True,
        }
    )
    ei_target: Optional[EiTarget] = field(
        default=None,
        metadata={
            "name": "eiTarget",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    signal_name: Optional[Union[SignalNameEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "signalName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"x-\S.*",
        }
    )
    signal_type: Optional[SignalTypeEnumeratedType] = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    signal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "signalID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
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
    current_value: Optional[CurrentValue] = field(
        default=None,
        metadata={
            "name": "currentValue",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class EiEventSignal(EiEventSignalType):
    class Meta:
        name = "eiEventSignal"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Interval(IntervalType):
    class Meta:
        name = "interval"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignalsType:
    """
    :ivar ei_event_signal: Interval data for an event
    :ivar ei_event_baseline: Interval data for a baseline
    """
    class Meta:
        name = "eiEventSignalsType"

    ei_event_signal: List[EiEventSignal] = field(
        default_factory=list,
        metadata={
            "name": "eiEventSignal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
        }
    )
    ei_event_baseline: Optional[EiEventBaseline] = field(
        default=None,
        metadata={
            "name": "eiEventBaseline",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class EiEventSignals(EiEventSignalsType):
    """
    Interval data for one or more event signals and/or baselines.
    """
    class Meta:
        name = "eiEventSignals"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventType:
    class Meta:
        name = "eiEventType"

    event_descriptor: Optional[EventDescriptor] = field(
        default=None,
        metadata={
            "name": "eventDescriptor",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    ei_active_period: Optional[EiActivePeriod] = field(
        default=None,
        metadata={
            "name": "eiActivePeriod",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    ei_event_signals: Optional[EiEventSignals] = field(
        default=None,
        metadata={
            "name": "eiEventSignals",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
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


@dataclass
class EiEvent(EiEventType):
    class Meta:
        name = "eiEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
