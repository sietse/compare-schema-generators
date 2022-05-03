from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from xsdata.models.datatype import XmlDateTime


@dataclass
class AggregatedPnodeType:
    """
    An aggregated pricing node is a specialized type of pricing node used to
    model items such as System Zone, Default Price Zone, Custom Price Zone,
    Control Area, Aggregated Generation, Aggregated Participating Load,
    Aggregated Non-Participating Load, Trading Hub, DCA Zone.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class EndDeviceAssetType:
    """
    The EndDeviceAssets are the physical device or devices which could be
    meters or other types of devices that may be of interest.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    mrid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class MeterAssetType:
    """
    The MeterAsset is the physical device or devices that performs the role of
    the meter.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    mrid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class PnodeType:
    """A pricing node is directly associated with a connectivity node.

    It is a pricing location for which market participants submit their
    bids, offers, buy/sell CRRs, and settle.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class PowerAttributesType:
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    hertz: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    ac: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


class PowerRealTypeItemUnits(Enum):
    W = "W"
    J_S = "J/s"


@dataclass
class ServiceDeliveryPointType:
    """Logical point on the network where the ownership of the service changes
    hands.

    It is one of potentially many service points within a
    ServiceLocation, delivering service in accordance with a
    CustomerAgreement. Used at the place where a meter may be installed.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class TransportInterfaceType:
    """
    The Transport Interface delineates the edges at either end of a transport
    segment.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    point_of_receipt: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfReceipt",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    point_of_delivery: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfDelivery",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class Mrid:
    class Meta:
        name = "mrid"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Node:
    class Meta:
        name = "node"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class SiScaleCodeType(Enum):
    """
    Scale based on representations of SI scale as expressed in the unit
    multipliers enumeration.

    :cvar P: Pico 10**-12
    :cvar N: Nano 10**-9
    :cvar MICRO: Micro 10**-6
    :cvar M: Milli 10**-3
    :cvar C: Centi 10**-2
    :cvar D: Deci 10**-1
    :cvar K: Kilo 10**3
    :cvar M_1: Mega 10**6
    :cvar G: Giga 10**9
    :cvar T: Tera 10**12
    :cvar NONE: Native Scale
    """
    P = "p"
    N = "n"
    MICRO = "micro"
    M = "m"
    C = "c"
    D = "d"
    K = "k"
    M_1 = "M"
    G = "G"
    T = "T"
    NONE = "none"


@dataclass
class ItemBaseType:
    """
    Abstract base type for units for EMIX Product delivery, measurement, and
    warrants.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06"


@dataclass
class MarketContext:
    """
    A URI identifying a DR Program.
    """
    class Meta:
        name = "marketContext"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class EiRequestEvent:
    """
    Request Event from a VTN in pull mode.

    :ivar request_id:
    :ivar ven_id:
    :ivar reply_limit: Limit the number of events contained in the
        oadrDistributeEvent payload
    """
    class Meta:
        name = "eiRequestEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestID",
            "type": "Element",
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
    reply_limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "replyLimit",
            "type": "Element",
        }
    )


@dataclass
class ReplyLimit:
    class Meta:
        name = "replyLimit"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReportToFollow:
    """
    Indicates if report (in the form of UpdateReport) to be returned following
    cancellation of Report.
    """
    class Meta:
        name = "reportToFollow"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequestId:
    """
    A ID used to match up a logical transaction request and response.
    """
    class Meta:
        name = "requestID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class EiResponseType:
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class QualifiedEventIdtype:
    """
    Fully qualified event ID includes the eventID and the modificationNumber.
    """
    class Meta:
        name = "QualifiedEventIDType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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


class AccumulationKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable, or implied by the unit of measure.
    :cvar VALUE_1: A value from a register which represents the bulk
        quantity of a commodity. This quantity is computed as the
        integral of the commodity usage rate. This value is typically
        used as the basis for the dial reading at the meter, and as a
        result, will roll over upon reaching a maximum dial value. Note
        1: With the metering system, the roll-over behaviour typically
        implies a roll-under behavior so that the value presented is
        always a positive value (e.g. unsigned integer or positive
        decimal.) However, when communicating data between enterprise
        applications a negative value might occur in a case such as net
        metering.Note 2: A BulkQuantity refers primarily to the dial
        reading and not the consumption over a specific period of time.
    :cvar VALUE_2: The sum of the previous billing period values and the
        present period value. Note: “ContinuousCumulative” is commonly
        used in conjunction with “demand.” The “ContinuousCumulative
        Demand” would be the cumulative sum of the previous billing
        period maximum demand values (as occurring with each demand
        reset) summed with the present period maximum demand value
        (which has yet to be reset.)
    :cvar VALUE_3: The sum of the previous billing period values. Note:
        “Cumulative” is commonly used in conjunction with “demand.” Each
        demand reset causes the maximum demand value for the present
        billing period (since the last demand reset) to accumulate as an
        accumulative total of all maximum demands. So instead of
        “zeroing” the demand register, a demand reset has the affect of
        adding the present maximum demand to this accumulating total.
    :cvar VALUE_4: The difference between the value at the end of the
        prescribed interval and the beginning of the interval. This is
        used for incremental interval data. Note: One common application
        would be for load profile data, another use might be to report
        the number of events within an interval (such as the number of
        equipment energizations within the specified period of time.)
    :cvar VALUE_6: As if a needle is swung out on the meter face to a
        value to indicate the current value. (Note: An “indicating”
        value is typically measured over hundreds of milliseconds or
        greater, or may imply a “pusher” mechanism to capture a value.
        Compare this to “instantaneous” which is measured over a shorter
        period of time.)
    :cvar VALUE_9: A form of accumulation which is selective with
        respect to time. Note : “Summation” could be considered a
        specialization of “Bulk Quantity” according to the rules of
        inheritance where “Summation” selectively accumulates pulses
        over a timing pattern, and “BulkQuantity” accumulates pulses all
        of the time.
    :cvar VALUE_10: A form of computation which introduces a time delay
        characteristic to the data value
    :cvar VALUE_12: Typically measured over the fastest period of time
        allowed by the definition of the metric (usually milliseconds or
        tens of milliseconds.) (Note: “Instantaneous” was moved to
        attribute #3 in 61968-9Ed2 from attribute #1 in 61968-9Ed1.)
    :cvar VALUE_13: When this description is applied to a metered value,
        it implies that the value is a time-independent cumulative
        quantity much a BulkQuantity, except that it latches upon the
        maximum value upon reaching that value. Any additional
        accumulation (positive or negative) is discarded until a reset
        occurs. Note: A LatchingQuantity may also occur in the downward
        direction – upon reaching a minimum value. The terms “maximum”
        or “minimum” will usually be included as an attribute when this
        type of accumulation behaviour is present.When this description
        is applied to an encoded value (UOM= “Code”), it implies that
        the value has one or more bits which are latching. The condition
        that caused the bit to be set may have long since evaporated.In
        either case, the timestamp that accompanies the value may not
        coincide with the moment the value was initially set.In both
        cases a system will need to perform an operation to clear the
        latched value.
    :cvar VALUE_14: A time-independent cumulative quantity much a
        BulkQuantity or a LatchingQuantity, except that the accumulation
        stops at the maximum or minimum values. When the maximum is
        reached, any additional positive accumulation is discarded, but
        negative accumulation may be accepted (thus lowering the
        counter.) Likewise, when the negative bound is reached, any
        additional negative accumulation is discarded, but positive
        accumulation is accepted (thus increasing the counter.)
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14


class CrudoperationValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CommodityKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_1: All types of metered quantities. This type of reading
        comes from the meter and represents a “secondary” metered value.
    :cvar VALUE_2: It is possible for a meter to be outfitted with an
        external VT and/or CT. The meter might not be aware of these
        devices, and the display not compensate for their presence.
        Ultimately, when these scalars are applied, the value that
        represents the service value is called the “primary metered”
        value. The “index” in sub-category 3 mirrors those of sub-
        category 0.
    :cvar VALUE_3: A measurement of the communication infrastructure
        itself.
    :cvar VALUE_4:
    :cvar VALUE_5: (SF6 is found separately below.)
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9: Drinkable water
    :cvar VALUE_10: Water in steam form, usually used for heating.
    :cvar VALUE_11: (Sewerage)
    :cvar VALUE_12: This fluid is likely in liquid form. It is not
        necessarily water or water based. The warm fluid returns cooler
        than when it was sent. The heat conveyed may be metered.
    :cvar VALUE_13: The cool fluid returns warmer than when it was sent.
        The heat conveyed may be metered.
    :cvar VALUE_14: Reclaimed water – possibly used for irrigation but
        not sufficiently treated to be considered safe for drinking.
    :cvar VALUE_15: Nitrous Oxides NOX
    :cvar VALUE_16: Sulfur Dioxide SO2
    :cvar VALUE_17: Methane CH4
    :cvar VALUE_18: Carbon Dioxide CO2
    :cvar VALUE_19:
    :cvar VALUE_20: Hexachlorocyclohexane HCH
    :cvar VALUE_21: Perfluorocarbons PFC
    :cvar VALUE_22: Sulfurhexafluoride SF6
    :cvar VALUE_23: Television
    :cvar VALUE_24: Internet service
    :cvar VALUE_25: trash
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25


class CurrencyValue(Enum):
    """
    :cvar VALUE_840: US dollar
    :cvar VALUE_978: European euro
    :cvar VALUE_36: Australian dollar
    :cvar VALUE_124: Canadian dollar
    :cvar VALUE_756: Swiss francs
    :cvar VALUE_156: Chinese yuan renminbi
    :cvar VALUE_208: Danish crown
    :cvar VALUE_826: British pound
    :cvar VALUE_392: Japanese yen
    :cvar VALUE_578: Norwegian crown
    :cvar VALUE_643: Russian ruble
    :cvar VALUE_752: Swedish crown
    :cvar VALUE_356: India rupees
    :cvar VALUE_0: Another type of currency.
    """
    VALUE_840 = 840
    VALUE_978 = 978
    VALUE_36 = 36
    VALUE_124 = 124
    VALUE_756 = 756
    VALUE_156 = 156
    VALUE_208 = 208
    VALUE_826 = 826
    VALUE_392 = 392
    VALUE_578 = 578
    VALUE_643 = 643
    VALUE_752 = 752
    VALUE_356 = 356
    VALUE_0 = 0


class DataQualifierKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_2: Average value
    :cvar VALUE_4: The value represents an amount over which a threshold
        was exceeded.
    :cvar VALUE_5: The value represents a programmed threshold.
    :cvar VALUE_7: The value represents a programmed threshold.
    :cvar VALUE_8: The highest value observed
    :cvar VALUE_9: The smallest value observed
    :cvar VALUE_11:
    :cvar VALUE_12:
    :cvar VALUE_16: The second highest value observed
    :cvar VALUE_17: The second smallest value observed
    :cvar VALUE_23: The third highest value observed
    :cvar VALUE_24: The fourth highest value observed
    :cvar VALUE_25: The fifth highest value observed
    :cvar VALUE_26: The accumulated sum
    """
    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26


class EspiserviceStatusValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


class FlowDirectionKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable (N/A)
    :cvar VALUE_1: "Delivered," or "Imported" as defined 61968-2.Forward
        Active Energy is a positive kWh value as one would naturally
        expect to find as energy is supplied by the utility and consumed
        at the service.Forward Reactive Energy is a positive VArh value
        as one would naturally expect to find in the presence of
        inductive loading.In polyphase metering, the forward energy
        register is incremented when the sum of the phase energies is
        greater than zero.
    :cvar VALUE_2: Typically used to describe that a power factor is
        lagging the reference value. Note 1: When used to describe VA,
        “lagging” describes a form of measurement where reactive power
        is considered in all four quadrants, but real power is
        considered only in quadrants I and IV.Note 2: When used to
        describe power factor, the term “Lagging” implies that the PF is
        negative. The term “lagging” in this case takes the place of the
        negative sign. If a signed PF value is to be passed by the data
        producer, then the direction of flow enumeration zero (none)
        should be used in order to avoid the possibility of creating an
        expression that employs a double negative. The data consumer
        should be able to tell from the sign of the data if the PF is
        leading or lagging. This principle is analogous to the concept
        that “Reverse” energy is an implied negative value, and to
        publish a negative reverse value would be ambiguous.Note 3:
        Lagging power factors typically indicate inductive loading.
    :cvar VALUE_3: Typically used to describe that a power factor is
        leading the reference value.Note: Leading power factors
        typically indicate capacitive loading.
    :cvar VALUE_4: |Forward| - |Reverse|, See 61968-2.Note: In some
        systems, the value passed as a “net” value could become
        negative. In other systems the value passed as a “net” value is
        always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar VALUE_5: Reactive positive quadrants. (The term “lagging” is
        preferred.)
    :cvar VALUE_7: Quadrants 1 and 3
    :cvar VALUE_8: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar VALUE_9: Q1 minus Q4
    :cvar VALUE_10: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar VALUE_11: Quadrants 2 and 4
    :cvar VALUE_12: Q2 minus Q3
    :cvar VALUE_13: Reactive negative quadrants. (The term “leading” is
        preferred.)
    :cvar VALUE_14: Q3 minus Q2
    :cvar VALUE_15: Q1 only
    :cvar VALUE_16: Q2 only
    :cvar VALUE_17: Q3 only
    :cvar VALUE_18: Q4 only
    :cvar VALUE_19: Reverse Active Energy is equivalent to "Received,"
        or "Exported" as defined in 61968-2.Reverse Active Energy is a
        positive kWh value as one would expect to find when energy is
        backfed by the service onto the utility network.Reverse Reactive
        Energy is a positive VArh value as one would expect to find in
        the presence of capacitive loading and a leading Power Factor.In
        polyphase metering, the reverse energy register is incremented
        when the sum of the phase energies is less than zero.Note: The
        value passed as a reverse value is always a positive value. It
        is understood by the label “reverse” that it represents negative
        flow.
    :cvar VALUE_20: |Forward| + |Reverse|, See 61968-2.The sum of the
        commodity in all quadrants Q1+Q2+Q3+Q4.In polyphase metering,
        the total energy register is incremented when the absolute value
        of the sum of the phase energies is greater than zero.
    :cvar VALUE_21: In polyphase metering, the total by phase energy
        register is incremented when the sum of the absolute values of
        the phase energies is greater than zero.In single phase
        metering, the formulas for “Total” and “Total by phase” collapse
        to the same expression. For communication purposes however, the
        “Total” enumeration should be used with single phase meter data.
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21


@dataclass
class LineItem:
    """
    [extension] Line item of detail for additional cost.
    """
    class Meta:
        target_namespace = "http://naesb.org/espi"

    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    rounding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )


class MeasurementKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_2:
    :cvar VALUE_3: funds
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    :cvar VALUE_10:
    :cvar VALUE_11:
    :cvar VALUE_12:
    :cvar VALUE_13:
    :cvar VALUE_14:
    :cvar VALUE_15:
    :cvar VALUE_16: Dup with “currency”
    :cvar VALUE_17:
    :cvar VALUE_18:
    :cvar VALUE_19:
    :cvar VALUE_20:
    :cvar VALUE_21:
    :cvar VALUE_22:
    :cvar VALUE_23:
    :cvar VALUE_24:
    :cvar VALUE_25:
    :cvar VALUE_26:
    :cvar VALUE_27:
    :cvar VALUE_28:
    :cvar VALUE_31:
    :cvar VALUE_32:
    :cvar VALUE_33:
    :cvar VALUE_34:
    :cvar VALUE_35:
    :cvar VALUE_36:
    :cvar VALUE_37:
    :cvar VALUE_38:
    :cvar VALUE_40:
    :cvar VALUE_41: or Voltage Dip
    :cvar VALUE_42:
    :cvar VALUE_43:
    :cvar VALUE_44:
    :cvar VALUE_45:
    :cvar VALUE_46:
    :cvar VALUE_47:
    :cvar VALUE_48:
    :cvar VALUE_49:
    :cvar VALUE_50:
    :cvar VALUE_51:
    :cvar VALUE_52:
    :cvar VALUE_53:
    :cvar VALUE_54:
    :cvar VALUE_55:
    :cvar VALUE_56:
    :cvar VALUE_57:
    :cvar VALUE_58: Clarified from Ed. 1. to indicate fluid volume
    :cvar VALUE_59:
    :cvar VALUE_60:
    :cvar VALUE_64:
    :cvar VALUE_81: Usually expressed as a “count”
    :cvar VALUE_90:
    :cvar VALUE_91:
    :cvar VALUE_92:
    :cvar VALUE_93:
    :cvar VALUE_94:
    :cvar VALUE_95:
    :cvar VALUE_96:
    :cvar VALUE_97:
    :cvar VALUE_98:
    :cvar VALUE_99:
    :cvar VALUE_100:
    :cvar VALUE_101:
    :cvar VALUE_102:
    :cvar VALUE_103:
    :cvar VALUE_104:
    :cvar VALUE_105:
    :cvar VALUE_106:
    :cvar VALUE_107:
    :cvar VALUE_108:
    :cvar VALUE_109:
    :cvar VALUE_110:
    :cvar VALUE_111:
    :cvar VALUE_112:
    :cvar VALUE_113:
    :cvar VALUE_114:
    :cvar VALUE_115:
    :cvar VALUE_116:
    :cvar VALUE_117: Moved here from Attribute #9 UOM
    :cvar VALUE_118:
    :cvar VALUE_119:
    :cvar VALUE_120:
    :cvar VALUE_121:
    :cvar VALUE_122: Usually expressed as a count as part of a billing
        cycle
    :cvar VALUE_123:
    :cvar VALUE_124:
    :cvar VALUE_125:
    :cvar VALUE_126:
    :cvar VALUE_127:
    :cvar VALUE_128:
    :cvar VALUE_129:
    :cvar VALUE_130:
    :cvar VALUE_131:
    :cvar VALUE_132:
    :cvar VALUE_133:
    :cvar VALUE_134:
    :cvar VALUE_135:
    :cvar VALUE_136:
    :cvar VALUE_137:
    :cvar VALUE_138:
    :cvar VALUE_139:
    :cvar VALUE_140:
    :cvar VALUE_141:
    :cvar VALUE_142: Usually expressed as a count
    :cvar VALUE_143:
    :cvar VALUE_144:
    :cvar VALUE_145:
    :cvar VALUE_146:
    :cvar VALUE_147:
    :cvar VALUE_148:
    :cvar VALUE_149:
    :cvar VALUE_150: Customer’s bill for the previous billing period
        (Currency)
    :cvar VALUE_151: Customer’s bill, as known thus far within the
        present billing period (Currency)
    :cvar VALUE_152: Customer’s bill for the (Currency)
    :cvar VALUE_153: Monthly fee for connection to commodity.
    :cvar VALUE_154: Sound
    :cvar VALUE_155:
    """
    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_64 = 64
    VALUE_81 = 81
    VALUE_90 = 90
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_95 = 95
    VALUE_96 = 96
    VALUE_97 = 97
    VALUE_98 = 98
    VALUE_99 = 99
    VALUE_100 = 100
    VALUE_101 = 101
    VALUE_102 = 102
    VALUE_103 = 103
    VALUE_104 = 104
    VALUE_105 = 105
    VALUE_106 = 106
    VALUE_107 = 107
    VALUE_108 = 108
    VALUE_109 = 109
    VALUE_110 = 110
    VALUE_111 = 111
    VALUE_112 = 112
    VALUE_113 = 113
    VALUE_114 = 114
    VALUE_115 = 115
    VALUE_116 = 116
    VALUE_117 = 117
    VALUE_118 = 118
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_121 = 121
    VALUE_122 = 122
    VALUE_123 = 123
    VALUE_124 = 124
    VALUE_125 = 125
    VALUE_126 = 126
    VALUE_127 = 127
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_134 = 134
    VALUE_135 = 135
    VALUE_136 = 136
    VALUE_137 = 137
    VALUE_138 = 138
    VALUE_139 = 139
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_143 = 143
    VALUE_144 = 144
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_147 = 147
    VALUE_148 = 148
    VALUE_149 = 149
    VALUE_150 = 150
    VALUE_151 = 151
    VALUE_152 = 152
    VALUE_153 = 153
    VALUE_154 = 154
    VALUE_155 = 155


@dataclass
class Object1:
    """
    Superclass of all object classes to allow extensions.

    :ivar extension: Contains an extension.
    """
    class Meta:
        name = "Object"
        namespace = "http://naesb.org/espi"

    extension: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


class PhaseCodeKindValue(Enum):
    """
    :cvar VALUE_225: ABC to Neutral
    :cvar VALUE_224: Involving all phases
    :cvar VALUE_193: AB to Neutral
    :cvar VALUE_97: Phases A, C and neutral.
    :cvar VALUE_132: Phases A to B
    :cvar VALUE_96: Phases A and C
    :cvar VALUE_66: Phases B to C
    :cvar VALUE_129: Phases A to neutral.
    :cvar VALUE_65: Phases B to neutral.
    :cvar VALUE_33: Phases C to neutral.
    :cvar VALUE_128: Phase A.
    :cvar VALUE_64: Phase B.
    :cvar VALUE_32: Phase C.
    :cvar VALUE_16: Neutral
    :cvar VALUE_272: Phase S2 to neutral.
    :cvar VALUE_784: Phase S1, S2 to neutral.
    :cvar VALUE_528: Phase S1 to Neutral
    :cvar VALUE_256: Phase S2.
    :cvar VALUE_768: Phase S1 to S2
    :cvar VALUE_0: Not applicable to any phase
    :cvar VALUE_136: Phase A current relative to Phase A voltage
    :cvar VALUE_72: Phase B current or voltage relative to Phase A
        voltage
    :cvar VALUE_41: CA to Neutral
    :cvar VALUE_40: hase C current or voltage relative to Phase A
        voltage
    :cvar VALUE_17: Neutral to ground
    :cvar VALUE_512: Phase S1
    """
    VALUE_225 = 225
    VALUE_224 = 224
    VALUE_193 = 193
    VALUE_97 = 97
    VALUE_132 = 132
    VALUE_96 = 96
    VALUE_66 = 66
    VALUE_129 = 129
    VALUE_65 = 65
    VALUE_33 = 33
    VALUE_128 = 128
    VALUE_64 = 64
    VALUE_32 = 32
    VALUE_16 = 16
    VALUE_272 = 272
    VALUE_784 = 784
    VALUE_528 = 528
    VALUE_256 = 256
    VALUE_768 = 768
    VALUE_0 = 0
    VALUE_136 = 136
    VALUE_72 = 72
    VALUE_41 = 41
    VALUE_40 = 40
    VALUE_17 = 17
    VALUE_512 = 512


class QualityOfReadingValue(Enum):
    """
    :cvar VALUE_0: data that has gone through all required validation
        checks and either passed them all or has been verified
    :cvar VALUE_7: Replaced or approved by a human
    :cvar VALUE_8: data value was replaced by a machine computed value
        based on analysis of historical data using the same type of
        measurement.
    :cvar VALUE_9: data value was computed using linear interpolation
        based on the readings before and after it
    :cvar VALUE_10: data that has failed one or more checks
    :cvar VALUE_11: data that has been calculated (using logic or
        mathematical operations)
    :cvar VALUE_12: data that has been calculated as a projection or
        forecast of future readings
    :cvar VALUE_13: indicates that the quality of this reading has mixed
        characteristics
    :cvar VALUE_14: data that has not gone through the validation
    :cvar VALUE_15: the values have been adjusted to account for weather
    :cvar VALUE_16: specifies that a characteristic applies other than
        those defined
    :cvar VALUE_17: data that has been validated and possibly edited
        and/or estimated in accordance with approved procedures
    :cvar VALUE_18: data that failed at least one of the required
        validation checks but was determined to represent actual usage
    """
    VALUE_0 = 0
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18


@dataclass
class RationalNumber:
    """[extension] Rational number = 'numerator' / 'denominator'."""
    class Meta:
        target_namespace = "http://naesb.org/espi"

    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )


@dataclass
class ReadingInterharmonic:
    """
    [extension] Interharmonics are represented as a rational number 'numerator'
    / 'denominator', and harmonics are represented using the same mechanism and
    identified by 'denominator'=1.
    """
    class Meta:
        target_namespace = "http://naesb.org/espi"

    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )


class ServiceKindValue(Enum):
    """
    :cvar VALUE_0: Electricity service.
    :cvar VALUE_1: Gas service.
    :cvar VALUE_2: Water service.
    :cvar VALUE_3: Time service.
    :cvar VALUE_4: Heat service.
    :cvar VALUE_5: Refuse (waster) service.
    :cvar VALUE_6: Sewerage service.
    :cvar VALUE_7: Rates (e.g. tax, charge, toll, duty, tariff, etc.)
        service.
    :cvar VALUE_8: TV license service.
    :cvar VALUE_9: Internet service.
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class StatusCodeValue(Enum):
    VALUE_200 = 200
    VALUE_201 = 201
    VALUE_204 = 204
    VALUE_301 = 301
    VALUE_302 = 302
    VALUE_304 = 304
    VALUE_400 = 400
    VALUE_401 = 401
    VALUE_403 = 403
    VALUE_404 = 404
    VALUE_405 = 405
    VALUE_410 = 410
    VALUE_500 = 500


class TimeAttributeKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_1: 10-minute
    :cvar VALUE_2: 15-minute
    :cvar VALUE_3: 1-minute
    :cvar VALUE_4: 24-hour
    :cvar VALUE_5: 30-minute
    :cvar VALUE_6: 5-minute
    :cvar VALUE_7: 60-minute
    :cvar VALUE_10: 2-minute
    :cvar VALUE_14: 3-minute
    :cvar VALUE_15: Within the present period of time
    :cvar VALUE_16: Shifted within the previous monthly cycle and data
        set
    :cvar VALUE_31: 20-minute interval
    :cvar VALUE_50: 60-minute Fixed Block
    :cvar VALUE_51: 30-minute Fixed Block
    :cvar VALUE_52: 20-minute Fixed Block
    :cvar VALUE_53: 15-minute Fixed Block
    :cvar VALUE_54: 10-minute Fixed Block
    :cvar VALUE_55: 5-minute Fixed Block
    :cvar VALUE_56: 1-minute Fixed Block
    :cvar VALUE_57: 60-minute Rolling Block with 30-minute sub-intervals
    :cvar VALUE_58: 60-minute Rolling Block with 20-minute sub-intervals
    :cvar VALUE_59: 60-minute Rolling Block with 15-minute sub-intervals
    :cvar VALUE_60: 60-minute Rolling Block with 12-minute sub-intervals
    :cvar VALUE_61: 60-minute Rolling Block with 10-minute sub-intervals
    :cvar VALUE_62: 60-minute Rolling Block with 6-minute sub-intervals
    :cvar VALUE_63: 60-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_64: 60-minute Rolling Block with 4-minute sub-intervals
    :cvar VALUE_65: 30-minute Rolling Block with 15-minute sub-intervals
    :cvar VALUE_66: 30-minute Rolling Block with 10-minute sub-intervals
    :cvar VALUE_67: 30-minute Rolling Block with 6-minute sub-intervals
    :cvar VALUE_68: 30-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_69: 30-minute Rolling Block with 3-minute sub-intervals
    :cvar VALUE_70: 30-minute Rolling Block with 2-minute sub-intervals
    :cvar VALUE_71: 15-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_72: 15-minute Rolling Block with 3-minute sub-intervals
    :cvar VALUE_73: 15-minute Rolling Block with 1-minute sub-intervals
    :cvar VALUE_74: 10-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_75: 10-minute Rolling Block with 2-minute sub-intervals
    :cvar VALUE_76: 10-minute Rolling Block with 1-minute sub-intervals
    :cvar VALUE_77: 5-minute Rolling Block with 1-minute sub-intervals
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_10 = 10
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_31 = 31
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64
    VALUE_65 = 65
    VALUE_66 = 66
    VALUE_67 = 67
    VALUE_68 = 68
    VALUE_69 = 69
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_75 = 75
    VALUE_76 = 76
    VALUE_77 = 77


class TimePeriodOfInterestValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_8: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar VALUE_11: Daily Period starting at midnight. If for the
        current day, this specifies the time from midnight to "now".
    :cvar VALUE_13: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar VALUE_22: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar VALUE_24: Weekly period starting at midnight on the first day
        of the week and ending the instant before midnight the last day
        of the week. If within the current week, it specifies the period
        from the start of the week until "now."
    :cvar VALUE_32: For the period defined by the start and end of the
        TimePeriod element in the message.
    """
    VALUE_0 = 0
    VALUE_8 = 8
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_22 = 22
    VALUE_24 = 24
    VALUE_32 = 32


class UnitMultiplierKindValue(Enum):
    """
    :cvar VALUE_MINUS_12: Pico 10**-12
    :cvar VALUE_MINUS_9: Nano 10**-9
    :cvar VALUE_MINUS_6: Micro 10**-6
    :cvar VALUE_MINUS_3: Milli 10**-3
    :cvar VALUE_MINUS_2: Centi 10**-2
    :cvar VALUE_MINUS_1: Deci 10**-1
    :cvar VALUE_3_1: Kilo 10**3
    :cvar VALUE_6_1: Mega 10**6
    :cvar VALUE_9_1: Giga 10**9
    :cvar VALUE_12_1: Tera 10**12
    :cvar VALUE_0: Not Applicable or "x1"
    :cvar VALUE_1_1: deca 10**1
    :cvar VALUE_2_1: hecto 10**2
    """
    VALUE_MINUS_12 = -12
    VALUE_MINUS_9 = -9
    VALUE_MINUS_6 = -6
    VALUE_MINUS_3 = -3
    VALUE_MINUS_2 = -2
    VALUE_MINUS_1 = -1
    VALUE_3_1 = 3
    VALUE_6_1 = 6
    VALUE_9_1 = 9
    VALUE_12_1 = 12
    VALUE_0 = 0
    VALUE_1_1 = 1
    VALUE_2_1 = 2


class UnitSymbolKindValue(Enum):
    """
    :cvar VALUE_61: Apparent power, Volt Ampere (See also real power and
        reactive power.), VA
    :cvar VALUE_38: Real power, Watt. By definition, one Watt equals
        oneJoule per second. Electrical power may have real and reactive
        components. The real portion of electrical power (I²R) or
        VIcos?, is expressed in Watts. (See also apparent power and
        reactive power.), W
    :cvar VALUE_63: Reactive power, Volt Ampere reactive. The “reactive”
        or “imaginary” component of electrical power (VISin?). (See also
        real power and apparent power)., VAr
    :cvar VALUE_71: Apparent energy, Volt Ampere hours, VAh
    :cvar VALUE_72: Real energy, Watt hours, Wh
    :cvar VALUE_73: Reactive energy, Volt Ampere reactive hours, VArh
    :cvar VALUE_29: Electric potential, Volt (W/A), V
    :cvar VALUE_30: Electric resistance, Ohm (V/A), O
    :cvar VALUE_5: Current, ampere, A
    :cvar VALUE_25: Electric capacitance, Farad (C/V), °C
    :cvar VALUE_28: Electric inductance, Henry (Wb/A), H
    :cvar VALUE_23: Relative temperature in degrees Celsius. In the SI
        unit system the symbol is ºC. Electric charge is measured in
        coulomb that has the unit symbol C. To destinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ºC is the special character º is difficult to
        manage in software.
    :cvar VALUE_27: Time, seconds, s
    :cvar VALUE_159: Time, minute = s * 60, min
    :cvar VALUE_160: Time, hour = minute * 60, h
    :cvar VALUE_9: Plane angle, degrees, deg
    :cvar VALUE_10: Plane angle, Radian (m/m), rad
    :cvar VALUE_31: Energy joule, (N·m = C·V = W·s), J
    :cvar VALUE_32: Force newton, (kg m/s²), N
    :cvar VALUE_53: Electric conductance, Siemens (A / V = 1 / O), S
    :cvar VALUE_0: N/A, None
    :cvar VALUE_33: Frequency hertz, (1/s), Hz
    :cvar VALUE_3: Mass in gram, g
    :cvar VALUE_39: Pressure, Pascal (N/m²)(Note: the absolute or
        relative measurement of pressure is implied with this entry. See
        below for more explicit forms.), Pa
    :cvar VALUE_2: Length, meter, m
    :cvar VALUE_41: Area, square meter, m²
    :cvar VALUE_42: Volume, cubic meter, m³
    :cvar VALUE_69: Amps squared, amp squared, A2
    :cvar VALUE_105: ampere-squared, Ampere-squared hour, A²h
    :cvar VALUE_70: Amps squared time, square amp second, A²s
    :cvar VALUE_106: Ampere-hours, Ampere-hours, Ah
    :cvar VALUE_152: Current, Ratio of Amperages, A/A
    :cvar VALUE_103: A/m, magnetic field strength, Ampere per metre, A/m
    :cvar VALUE_68: Amp seconds, amp seconds, As
    :cvar VALUE_79: Sound pressure level, Bel, acoustic, Combine with
        multiplier prefix “d” to form decibels of Sound Pressure
        Level“dB (SPL).”, B (SPL)
    :cvar VALUE_113: Signal Strength, Bel-mW, normalized to 1mW. Note:
        to form “dBm” combine “Bm” with multiplier “d”. Bm
    :cvar VALUE_22: Radioactivity, Becquerel (1/s), Bq
    :cvar VALUE_132: Energy, British Thermal Units, BTU
    :cvar VALUE_133: Power, BTU per hour, BTU/h
    :cvar VALUE_8: Luminous intensity, candela, cd
    :cvar VALUE_76: Number of characters, characters, char
    :cvar VALUE_75: Rate of change of frequency, hertz per second, Hz/s
    :cvar VALUE_114: Application Value, encoded value, code
    :cvar VALUE_65: Power factor, Dimensionless <ns1:img
        xmlns:ns1="http://naesb.org/espi" src="HTS_1.PNG" width="64"
        height="29" border="0" alt="graphic"/>, cos?
    :cvar VALUE_111: Amount of substance, counter value, count
    :cvar VALUE_119: Volume, cubic feet, ft³
    :cvar VALUE_120: Volume, cubic feet, ft³(compensated)
    :cvar VALUE_123: Volumetric flow rate, compensated cubic feet per
        hour, ft³(compensated)/h
    :cvar VALUE_78: Turbine inertia, gram·meter2 (Combine with
        multiplier prefix “k” to form kg·m2.), gm²
    :cvar VALUE_144: Concentration, The ratio of the mass of a solute
        divided by the mass of the solution., g/g
    :cvar VALUE_21: Absorbed dose, Gray (J/kg), GY
    :cvar VALUE_150: Frequency, Rate of frequency change, Hz/Hz
    :cvar VALUE_77: Data rate, characters per second, char/s
    :cvar VALUE_130: Volume, imperial gallons, ImperialGal
    :cvar VALUE_131: Volumetric flow rate, Imperial gallons per hour,
        ImperialGal/h
    :cvar VALUE_51: Heat capacity, Joule/Kelvin, J/K
    :cvar VALUE_165: Specific energy, Joules / kg, J/kg
    :cvar VALUE_6: Temperature, Kelvin, K
    :cvar VALUE_158: Catalytic activity, katal = mol / s, kat
    :cvar VALUE_47: Moment of mass ,kilogram meter (kg·m), M
    :cvar VALUE_48: Density, gram/cubic meter (combine with prefix
        multiplier “k” to form kg/ m³), g/m³
    :cvar VALUE_134: Volume, litre = dm3 = m3/1000., L
    :cvar VALUE_157: Volume, litre, with the value compensated for
        weather effects, L(compensated)
    :cvar VALUE_138: Volumetric flow rate, litres (compensated) per
        hour, L(compensated)/h
    :cvar VALUE_137: Volumetric flow rate, litres per hour, L/h
    :cvar VALUE_143: Concentration, The ratio of the volume of a solute
        divided by the volume of the solution., L/L
    :cvar VALUE_82: Volumetric flow rate, Volumetric flow rate, L/s
    :cvar VALUE_156: Volume, litre, with the value uncompensated for
        weather effects., L(uncompensated)
    :cvar VALUE_139: Volumetric flow rate, litres (uncompensated) per
        hour, L(uncompensated)/h
    :cvar VALUE_35: Luminous flux, lumen (cd sr), Lm
    :cvar VALUE_34: Illuminance lux, (lm/m²), L(uncompensated)/h
    :cvar VALUE_49: Viscosity, meter squared / second, m²/s
    :cvar VALUE_167: Volume, cubic meter, with the value compensated for
        weather effects., m3(compensated)
    :cvar VALUE_126: Volumetric flow rate, compensated cubic meters per
        hour, ³(compensated)/h
    :cvar VALUE_125: Volumetric flow rate, cubic meters per hour, m³/h
    :cvar VALUE_45: m3PerSec, cubic meters per second, m³/s
    :cvar VALUE_166: m3uncompensated, cubic meter, with the value
        uncompensated for weather effects., m3(uncompensated)
    :cvar VALUE_127: Volumetric flow rate, uncompensated cubic meters
        per hour, m³(uncompensated)/h
    :cvar VALUE_118: EndDeviceEvent, value to be interpreted as a
        EndDeviceEventCode, meCode
    :cvar VALUE_7: Amount of substance, mole, mol
    :cvar VALUE_147: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms., mol/kg
    :cvar VALUE_145: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in m³., mol/ m³
    :cvar VALUE_146: Concentration, Molar fraction (?), the ratio of the
        molar amount of a solute divided by the molar amount of the
        solution.,mol/mol
    :cvar VALUE_80: Monetary unit, Generic money (Note: Specific
        monetary units are identified the currency class)., ¤
    :cvar VALUE_148: Length, Ratio of length, m/m
    :cvar VALUE_46: Fuel efficiency, meters / cubic meter, m/m³
    :cvar VALUE_43: Velocity, meters per second (m/s), m/s
    :cvar VALUE_44: Acceleration, meters per second squared, m/s²
    :cvar VALUE_102: resistivity, ? (rho), ?m
    :cvar VALUE_155: Pressure, Pascal, absolute pressure, PaA
    :cvar VALUE_140: Pressure, Pascal, gauge pressure, PaG
    :cvar VALUE_141: Pressure, Pounds per square inch, absolute, psiA
    :cvar VALUE_142: Pressure, Pounds per square inch, gauge, psiG
    :cvar VALUE_100: Quantity power, Q, Q
    :cvar VALUE_161: Quantity power, Q measured at 45º, Q45
    :cvar VALUE_163: Quantity energy, Q measured at 45º, Q45h
    :cvar VALUE_162: Quantity power, Q measured at 60º, Q60
    :cvar VALUE_164: Quantity energy, Qh measured at 60º, Q60h
    :cvar VALUE_101: Quantity energy, Qh, Qh
    :cvar VALUE_54: Angular velocity, radians per second, rad/s
    :cvar VALUE_154: Amount of rotation, Revolutions, rev
    :cvar VALUE_4: Rotational speed, Rotations per second, rev/s
    :cvar VALUE_149: Time, Ratio of time (can be combined with an
        multiplier prefix to show rates such as a clock drift rate, e.g.
        “µs/s”), s/s
    :cvar VALUE_11: Solid angle, Steradian (m2/m2), sr
    :cvar VALUE_109: State, "1" = "true", "live", "on", "high", "set";
        "0" = "false", "dead", "off", "low", "cleared"Note: A Boolean
        value is preferred but other values may be supported, status
    :cvar VALUE_24: Doe equivalent, Sievert (J/kg), Sv
    :cvar VALUE_37: Magnetic flux density, Tesla (Wb/m2), T
    :cvar VALUE_169: Energy, Therm, therm
    :cvar VALUE_108: Timestamp, time and date per ISO 8601 format,
        timeStamp
    :cvar VALUE_128: Volume, US gallons, Gal
    :cvar VALUE_129: Volumetric flow rate, US gallons per hour, USGal/h
    :cvar VALUE_67: Volts squared, Volt squared (W2/A2), V²
    :cvar VALUE_104: volt-squared hour, Volt-squared-hours, V²h
    :cvar VALUE_117: Kh-Vah, apparent energy metering constant, VAh/rev
    :cvar VALUE_116: Kh-VArh, reactive energy metering constant,
        VArh/rev
    :cvar VALUE_74: Magnetic flux, Volts per Hertz, V/Hz
    :cvar VALUE_151: Voltage, Ratio of voltages (e.g. mV/V), V/V
    :cvar VALUE_66: Volt seconds, Volt seconds (Ws/A), Vs
    :cvar VALUE_36: Magnetic flux, Weber (V s), Wb
    :cvar VALUE_107: Wh/m3, energy per volume, Wh/m³
    :cvar VALUE_115: Kh-Wh, active energy metering constant, Wh/rev
    :cvar VALUE_50: Thermal conductivity, Watt/meter Kelvin, W/m K
    :cvar VALUE_81: Ramp rate, Watts per second, W/s
    :cvar VALUE_153: Power Factor, PF, W/VA
    :cvar VALUE_168: Signal Strength, Ratio of power, W/W
    """
    VALUE_61 = 61
    VALUE_38 = 38
    VALUE_63 = 63
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_5 = 5
    VALUE_25 = 25
    VALUE_28 = 28
    VALUE_23 = 23
    VALUE_27 = 27
    VALUE_159 = 159
    VALUE_160 = 160
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_53 = 53
    VALUE_0 = 0
    VALUE_33 = 33
    VALUE_3 = 3
    VALUE_39 = 39
    VALUE_2 = 2
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_69 = 69
    VALUE_105 = 105
    VALUE_70 = 70
    VALUE_106 = 106
    VALUE_152 = 152
    VALUE_103 = 103
    VALUE_68 = 68
    VALUE_79 = 79
    VALUE_113 = 113
    VALUE_22 = 22
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_8 = 8
    VALUE_76 = 76
    VALUE_75 = 75
    VALUE_114 = 114
    VALUE_65 = 65
    VALUE_111 = 111
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_123 = 123
    VALUE_78 = 78
    VALUE_144 = 144
    VALUE_21 = 21
    VALUE_150 = 150
    VALUE_77 = 77
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_51 = 51
    VALUE_165 = 165
    VALUE_6 = 6
    VALUE_158 = 158
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_134 = 134
    VALUE_157 = 157
    VALUE_138 = 138
    VALUE_137 = 137
    VALUE_143 = 143
    VALUE_82 = 82
    VALUE_156 = 156
    VALUE_139 = 139
    VALUE_35 = 35
    VALUE_34 = 34
    VALUE_49 = 49
    VALUE_167 = 167
    VALUE_126 = 126
    VALUE_125 = 125
    VALUE_45 = 45
    VALUE_166 = 166
    VALUE_127 = 127
    VALUE_118 = 118
    VALUE_7 = 7
    VALUE_147 = 147
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_80 = 80
    VALUE_148 = 148
    VALUE_46 = 46
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_102 = 102
    VALUE_155 = 155
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_100 = 100
    VALUE_161 = 161
    VALUE_163 = 163
    VALUE_162 = 162
    VALUE_164 = 164
    VALUE_101 = 101
    VALUE_54 = 54
    VALUE_154 = 154
    VALUE_4 = 4
    VALUE_149 = 149
    VALUE_11 = 11
    VALUE_109 = 109
    VALUE_24 = 24
    VALUE_37 = 37
    VALUE_169 = 169
    VALUE_108 = 108
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_67 = 67
    VALUE_104 = 104
    VALUE_117 = 117
    VALUE_116 = 116
    VALUE_74 = 74
    VALUE_151 = 151
    VALUE_66 = 66
    VALUE_36 = 36
    VALUE_107 = 107
    VALUE_115 = 115
    VALUE_50 = 50
    VALUE_81 = 81
    VALUE_153 = 153
    VALUE_168 = 168


@dataclass
class NonceValueType:
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    encoding_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "EncodingType",
            "type": "Attribute",
        }
    )


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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class FeatureCollection:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    location: Optional["FeatureCollection.Location"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )

    @dataclass
    class Location:
        polygon: Optional["FeatureCollection.Location.Polygon"] = field(
            default=None,
            metadata={
                "name": "Polygon",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class Polygon:
            exterior: Optional["FeatureCollection.Location.Polygon.Exterior"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.opengis.net/gml/3.2",
                }
            )

            @dataclass
            class Exterior:
                linear_ring: Optional["FeatureCollection.Location.Polygon.Exterior.LinearRing"] = field(
                    default=None,
                    metadata={
                        "name": "LinearRing",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class LinearRing:
                    pos_list: List[float] = field(
                        default_factory=list,
                        metadata={
                            "name": "posList",
                            "type": "Element",
                            "required": True,
                            "tokens": True,
                        }
                    )


@dataclass
class PosList:
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class CanonicalizationMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    q: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    g: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "G",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    y: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    j: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "J",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    pgen_counter: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PgenCounter",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )


@dataclass
class DigestMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DigestValue:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class KeyName:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class MgmtData:
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ObjectType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Attribute",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class PgpdataType:
    class Meta:
        name = "PGPDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    pgpkey_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PGPKeyID",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "format": "base64",
        }
    )
    pgpkey_packet: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "PGPKeyPacket",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class RsakeyValueType:
    class Meta:
        name = "RSAKeyValueType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    modulus: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Modulus",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    exponent: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Exponent",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class SpkidataType:
    class Meta:
        name = "SPKIDataType"
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    spkisexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SPKISexp",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
            "sequential": True,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )


@dataclass
class SignatureMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "HMACOutputLength",
                    "type": int,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class SignaturePropertyType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class SignatureValueType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TransformType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "XPath",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class X509IssuerSerialType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_issuer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509IssuerName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    x509_serial_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class CategoryType:
    """
    The Atom category construct is defined in section 4.2.2 of the format spec.
    """
    class Meta:
        name = "categoryType"
        target_namespace = "http://www.w3.org/2005/Atom"

    term: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ContentType:
    """
    The Atom content construct is defined in section 4.1.3 of the format spec.
    """
    class Meta:
        name = "contentType"
        target_namespace = "http://www.w3.org/2005/Atom"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DateTimeType:
    class Meta:
        name = "dateTimeType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class GeneratorType:
    """
    The Atom generator element is defined in section 4.2.4 of the format spec.
    """
    class Meta:
        name = "generatorType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class IconType:
    """
    The Atom icon construct is defined in section 4.2.5 of the format spec.
    """
    class Meta:
        name = "iconType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class IdType:
    """
    The Atom id construct is defined in section 4.2.6 of the format spec.
    """
    class Meta:
        name = "idType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class LinkType:
    """
    The Atom link construct is defined in section 3.4 of the format spec.
    """
    class Meta:
        name = "linkType"
        target_namespace = "http://www.w3.org/2005/Atom"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class LogoType:
    """
    The Atom logo construct is defined in section 4.2.8 of the format spec.
    """
    class Meta:
        name = "logoType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


class TextTypeType(Enum):
    TEXT = "text"
    HTML = "html"
    XHTML = "xhtml"


@dataclass
class UriType:
    class Meta:
        name = "uriType"
        target_namespace = "http://www.w3.org/2005/Atom"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class CharTwoFieldParamsType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    m: Optional[int] = field(
        default=None,
        metadata={
            "name": "M",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class CurveType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    a: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    b: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "B",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class DerencodedKeyValueType:
    class Meta:
        name = "DEREncodedKeyValueType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class EcvalidationDataType:
    class Meta:
        name = "ECValidationDataType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    hash_algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "hashAlgorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KeyInfoReferenceType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class NamedCurveType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrimeFieldParamsType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class X509DigestType:
    class Meta:
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class StreamPayloadBaseType:
    """Abstract class to convey a payload for a stream.

    When a Stream is transformed to or from a WS-Calendar Interval, the
    contents of the Stream Payload defined element are transformed into
    the contents of a WS-Calendar artifactBase.
    """
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0:stream"


@dataclass
class DurationPropType:
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )


@dataclass
class Components:
    class Meta:
        name = "components"
        nillable = True
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class DateTime:
    class Meta:
        name = "date-time"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Dtend:
    class Meta:
        name = "dtend"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Dtstart:
    """
    The starting time for the activity, data, or state change.
    """
    class Meta:
        name = "dtstart"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Text:
    class Meta:
        name = "text"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Uid:
    """
    Used as an index to identify intervals.
    """
    class Meta:
        name = "uid"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Iso3AlphaCurrencyCodeContentType(Enum):
    """
    :cvar AED: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UAE
        Dirham</ns1:Name>
    :cvar AFN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Afghani</ns1:Name>
    :cvar ALL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lek</ns1:Name>
    :cvar AMD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Armenian
        Dram</ns1:Name>
    :cvar ANG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Netherlands
        Antillian Guilder</ns1:Name>
    :cvar AOA: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kwanza</ns1:Name>
    :cvar ARS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Argentine
        Peso</ns1:Name>
    :cvar AUD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Australian
        Dollar</ns1:Name>
    :cvar AWG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Aruban
        Guilder</ns1:Name>
    :cvar AZN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Azerbaijanian
        Manat</ns1:Name>
    :cvar BAM: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Convertible
        Marks</ns1:Name>
    :cvar BBD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Barbados
        Dollar</ns1:Name>
    :cvar BDT: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Taka</ns1:Name>
    :cvar BGN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bulgarian
        Lev</ns1:Name>
    :cvar BHD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bahraini
        Dinar</ns1:Name>
    :cvar BIF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Burundi
        Franc</ns1:Name>
    :cvar BMD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bermudian
        Dollar (customarily known as Bermuda Dollar)</ns1:Name>
    :cvar BND: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Brunei
        Dollar</ns1:Name>
    :cvar BOB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Boliviano</ns1:Name>
    :cvar BOV: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Mvdol</ns1:Name>
    :cvar BRL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Brazilian
        Real</ns1:Name>
    :cvar BSD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bahamian
        Dollar</ns1:Name>
    :cvar BTN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Ngultrum</ns1:Name>
    :cvar BWP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Pula</ns1:Name>
    :cvar BYR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Belarussian
        Ruble</ns1:Name>
    :cvar BZD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Belize
        Dollar</ns1:Name>
    :cvar CAD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Canadian
        Dollar</ns1:Name>
    :cvar CDF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Congolese
        Franc</ns1:Name>
    :cvar CHE: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">WIR
        Euro</ns1:Name>
    :cvar CHF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Swiss
        Franc</ns1:Name>
    :cvar CHW: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">WIR
        Franc</ns1:Name>
    :cvar CLF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Unidades
        de fomento</ns1:Name>
    :cvar CLP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Chilean
        Peso</ns1:Name>
    :cvar CNY: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Yuan
        Renminbi</ns1:Name>
    :cvar COP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Colombian
        Peso</ns1:Name>
    :cvar COU: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Unidad
        de Valor Real</ns1:Name>
    :cvar CRC: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Costa
        Rican Colon</ns1:Name>
    :cvar CUC: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Peso
        Convertible</ns1:Name>
    :cvar CUP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Cuban
        Peso</ns1:Name>
    :cvar CVE: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Cape
        Verde Escudo</ns1:Name>
    :cvar CZK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Czech
        Koruna</ns1:Name>
    :cvar DJF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Djibouti
        Franc</ns1:Name>
    :cvar DKK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Danish
        Krone</ns1:Name>
    :cvar DOP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Dominican
        Peso</ns1:Name>
    :cvar DZD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Algerian
        Dinar</ns1:Name>
    :cvar EEK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kroon</ns1:Name>
    :cvar EGP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Egyptian
        Pound</ns1:Name>
    :cvar ERN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Nakfa</ns1:Name>
    :cvar ETB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Ethiopian
        Birr</ns1:Name>
    :cvar EUR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Euro</ns1:Name>
    :cvar FJD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Fiji
        Dollar</ns1:Name>
    :cvar FKP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Falkland
        Islands Pound</ns1:Name>
    :cvar GBP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Pound
        Sterling</ns1:Name>
    :cvar GEL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lari</ns1:Name>
    :cvar GHS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Cedi</ns1:Name>
    :cvar GIP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Gibraltar
        Pound</ns1:Name>
    :cvar GMD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Dalasi</ns1:Name>
    :cvar GNF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Guinea
        Franc</ns1:Name>
    :cvar GTQ: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Quetzal</ns1:Name>
    :cvar GWP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Guinea-
        Bissau Peso</ns1:Name>
    :cvar GYD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Guyana
        Dollar</ns1:Name>
    :cvar HKD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Hong
        Kong Dollar</ns1:Name>
    :cvar HNL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lempira</ns1:Name>
    :cvar HRK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Croatian
        Kuna</ns1:Name>
    :cvar HTG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Gourde</ns1:Name>
    :cvar HUF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Forint</ns1:Name>
    :cvar IDR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Rupiah</ns1:Name>
    :cvar ILS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">New
        Israeli Sheqel</ns1:Name>
    :cvar INR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Indian
        Rupee</ns1:Name>
    :cvar IQD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Iraqi
        Dinar</ns1:Name>
    :cvar IRR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Iranian
        Rial</ns1:Name>
    :cvar ISK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Iceland
        Krona</ns1:Name>
    :cvar JMD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Jamaican
        Dollar</ns1:Name>
    :cvar JOD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Jordanian
        Dinar</ns1:Name>
    :cvar JPY: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Yen</ns1:Name>
    :cvar KES: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kenyan
        Shilling</ns1:Name>
    :cvar KGS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Som</ns1:Name>
    :cvar KHR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Riel</ns1:Name>
    :cvar KMF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Comoro
        Franc</ns1:Name>
    :cvar KPW: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">North
        Korean Won</ns1:Name>
    :cvar KRW: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Won</ns1:Name>
    :cvar KWD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kuwaiti
        Dinar</ns1:Name>
    :cvar KYD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Cayman
        Islands Dollar</ns1:Name>
    :cvar KZT: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Tenge</ns1:Name>
    :cvar LAK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kip</ns1:Name>
    :cvar LBP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lebanese
        Pound</ns1:Name>
    :cvar LKR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Sri
        Lanka Rupee</ns1:Name>
    :cvar LRD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Liberian
        Dollar</ns1:Name>
    :cvar LSL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Loti</ns1:Name>
    :cvar LTL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lithuanian
        Litas</ns1:Name>
    :cvar LVL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Latvian
        Lats</ns1:Name>
    :cvar LYD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Libyan
        Dinar</ns1:Name>
    :cvar MAD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Moroccan
        Dirham</ns1:Name>
    :cvar MDL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Moldovan
        Leu</ns1:Name>
    :cvar MGA: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Malagasy
        Ariary</ns1:Name>
    :cvar MKD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Denar</ns1:Name>
    :cvar MMK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kyat</ns1:Name>
    :cvar MNT: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Tugrik</ns1:Name>
    :cvar MOP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Pataca</ns1:Name>
    :cvar MRO: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Ouguiya</ns1:Name>
    :cvar MUR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Mauritius
        Rupee</ns1:Name>
    :cvar MVR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Rufiyaa</ns1:Name>
    :cvar MWK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kwacha</ns1:Name>
    :cvar MXN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Mexican
        Peso</ns1:Name>
    :cvar MXV: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Mexican
        Unidad de Inversion (UDI)</ns1:Name>
    :cvar MYR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Malaysian
        Ringgit</ns1:Name>
    :cvar MZN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Metical</ns1:Name>
    :cvar NAD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Namibia
        Dollar</ns1:Name>
    :cvar NGN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Naira</ns1:Name>
    :cvar NIO: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Cordoba
        Oro</ns1:Name>
    :cvar NOK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Norwegian
        Krone</ns1:Name>
    :cvar NPR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Nepalese
        Rupee</ns1:Name>
    :cvar NZD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">New
        Zealand Dollar</ns1:Name>
    :cvar OMR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Rial
        Omani</ns1:Name>
    :cvar PAB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Balboa</ns1:Name>
    :cvar PEN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Nuevo
        Sol</ns1:Name>
    :cvar PGK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Kina</ns1:Name>
    :cvar PHP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Philippine
        Peso</ns1:Name>
    :cvar PKR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Pakistan
        Rupee</ns1:Name>
    :cvar PLN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Zloty</ns1:Name>
    :cvar PYG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Guarani</ns1:Name>
    :cvar QAR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Qatari
        Rial</ns1:Name>
    :cvar RON: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">New
        Leu</ns1:Name>
    :cvar RSD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Serbian
        Dinar</ns1:Name>
    :cvar RUB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Russian
        Ruble</ns1:Name>
    :cvar RWF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Rwanda
        Franc</ns1:Name>
    :cvar SAR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Saudi
        Riyal</ns1:Name>
    :cvar SBD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Solomon
        Islands Dollar</ns1:Name>
    :cvar SCR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Seychelles
        Rupee</ns1:Name>
    :cvar SDG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Sudanese
        Pound</ns1:Name>
    :cvar SEK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Swedish
        Krona</ns1:Name>
    :cvar SGD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Singapore
        Dollar</ns1:Name>
    :cvar SHP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Saint
        Helena Pound</ns1:Name>
    :cvar SLL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Leone</ns1:Name>
    :cvar SOS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Somali
        Shilling</ns1:Name>
    :cvar SRD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Surinam
        Dollar</ns1:Name>
    :cvar STD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Dobra</ns1:Name>
    :cvar SVC: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">El
        Salvador Colon</ns1:Name>
    :cvar SYP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Syrian
        Pound</ns1:Name>
    :cvar SZL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Lilangeni</ns1:Name>
    :cvar THB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Baht</ns1:Name>
    :cvar TJS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Somoni</ns1:Name>
    :cvar TMT: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Manat</ns1:Name>
    :cvar TND: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Tunisian
        Dinar</ns1:Name>
    :cvar TOP: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Pa'anga</ns1:Name>
    :cvar TRY: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Turkish
        Lira</ns1:Name>
    :cvar TTD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Trinidad
        and Tobago Dollar</ns1:Name>
    :cvar TWD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">New
        Taiwan Dollar</ns1:Name>
    :cvar TZS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Tanzanian
        Shilling</ns1:Name>
    :cvar UAH: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Hryvnia</ns1:Name>
    :cvar UGX: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Uganda
        Shilling</ns1:Name>
    :cvar USD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">US
        Dollar</ns1:Name>
    :cvar USN: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">US
        Dollar (Next day)</ns1:Name>
    :cvar USS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">US
        Dollar (Same day)</ns1:Name>
    :cvar UYI: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Uruguay
        Peso en Unidades Indexadas</ns1:Name>
    :cvar UYU: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Peso
        Uruguayo</ns1:Name>
    :cvar UZS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Uzbekistan
        Sum</ns1:Name>
    :cvar VEF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bolivar
        Fuerte</ns1:Name>
    :cvar VND: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Dong</ns1:Name>
    :cvar VUV: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Vatu</ns1:Name>
    :cvar WST: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Tala</ns1:Name>
    :cvar XAF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CFA
        Franc BEAC</ns1:Name>
    :cvar XAG: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Silver</ns1:Name>
    :cvar XAU: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Gold</ns1:Name>
    :cvar XBA: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Bond
        Markets Units European Composite Unit (EURCO)</ns1:Name>
    :cvar XBB: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">European
        Monetary Unit (E.M.U.-6)</ns1:Name>
    :cvar XBC: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">European
        Unit of Account 9(E.U.A.-9)</ns1:Name>
    :cvar XBD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">European
        Unit of Account 17(E.U.A.-17)</ns1:Name>
    :cvar XCD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">East
        Caribbean Dollar</ns1:Name>
    :cvar XDR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">SDR</ns1:Name>
    :cvar XFU: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">UIC-
        Franc</ns1:Name>
    :cvar XOF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CFA
        Franc BCEAO †</ns1:Name>
    :cvar XPD: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Palladium</ns1:Name>
    :cvar XPF: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">CFP
        Franc</ns1:Name>
    :cvar XPT: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Platinum</ns1:Name>
    :cvar XTS: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Codes
        specifically reserved for testing purposes</ns1:Name>
    :cvar XXX: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        codes assigned for transactions where no currency is involved
        are:</ns1:Name>
    :cvar YER: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Yemeni
        Rial</ns1:Name>
    :cvar ZAR: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Rand</ns1:Name>
    :cvar ZMK: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Zambian
        Kwacha</ns1:Name>
    :cvar ZWL: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Zimbabwe
        Dollar</ns1:Name>
    """
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GWP = "GWP"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    USS = "USS"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XFU = "XFU"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XTS = "XTS"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWL = "ZWL"


@dataclass
class EnergyItemType(ItemBaseType):
    """
    Base for the measurement of Energy.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
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
class ServiceLocationType:
    """A customer ServiceLocation has one or more ServiceDeliveryPoint(s),
    which in turn relate to Meters.

    The location may be a point or a polygon, depending on the specific
    circumstances. For distribution, the ServiceLocation is typically
    the location of the utility customer's premise.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class VoltageType(ItemBaseType):
    """
    Voltage.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="Voltage",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="V",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
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
class AggregatedPnode(AggregatedPnodeType):
    class Meta:
        name = "aggregatedPnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EndDeviceAsset(EndDeviceAssetType):
    class Meta:
        name = "endDeviceAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class MeterAsset(MeterAssetType):
    class Meta:
        name = "meterAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Pnode(PnodeType):
    class Meta:
        name = "pnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerAttributes(PowerAttributesType):
    class Meta:
        name = "powerAttributes"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceDeliveryPoint(ServiceDeliveryPointType):
    class Meta:
        name = "serviceDeliveryPoint"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class TransportInterface(TransportInterfaceType):
    class Meta:
        name = "transportInterface"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class SiScaleCode:
    class Meta:
        name = "siScaleCode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/siscale"

    value: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ServiceAreaType:
    """
    The Service Area is the geographic region that is affected by the EMIX
    market condition.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06"

    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    response: List[EiResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class PayloadFloatType(PayloadBaseType):
    """
    This is the payload for signals that require a quantity.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class BatchItemInfo(Object1):
    """
    Includes elements that make it possible to include multiple transactions in
    a single (batch) request.

    :ivar name: An identifier for this object that is only unique within
        the containing collection.
    :ivar operation: Specifies the operation requested of this item.
    :ivar status_code: Indicates the status code of the associated
        transaction.
    :ivar status_reason: Indicates the reason for the indicated status
        code.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    name: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    operation: Optional[Union[int, CrudoperationValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    status_code: Optional[Union[int, StatusCodeValue]] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
        }
    )
    status_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusReason",
            "type": "Element",
            "max_length": 256,
        }
    )


@dataclass
class DateTimeInterval(Object1):
    """Interval of date and time.

    End is not included because it can be derived from the start and the
    duration.

    :ivar duration: [correction] Duration of the interval, in seconds.
    :ivar start: [correction] Date and time that this interval started.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ReadingQuality(Object1):
    """Quality of a specific reading value or interval reading value.

    Note that more than one Quality may be applicable to a given
    Reading. Typically not used unless problems or unusual conditions
    occur (i.e., quality for each Reading is assumed to be 'Good'
    (valid) unless stated otherwise in associated ReadingQuality).

    :ivar quality: Quality, to be specified if different than
        ReadingType.defaultQuality. The specific format is specified per
        the standard is defined in QualityOfReading.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ServiceCategory(Object1):
    """
    Category of service provided to the customer.

    :ivar kind: Service classification Examples are: 0 - electricity 1 -
        gas The list of specific valid values per the standard are
        itemized in ServiceKind.
    """
    class Meta:
        target_namespace = "http://naesb.org/espi"

    kind: Optional[Union[int, ServiceKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


@dataclass
class ServiceDeliveryPoint1(Object1):
    """
    [extension] Service Delivery Point is representation of revenue UsagePoint
    attributes.

    :ivar name: The name is any free human readable and possibly non
        unique text naming the object.
    :ivar tariff_profile: A schedule of charges; structure associated
        with Tariff that allows the definition of complex tariff
        structures such as step and time of use.
    :ivar customer_agreement: Agreement between the customer and the
        ServiceSupplier to pay for service at a specific service
        location. It provides for the recording of certain billing
        information about the type of service provided at the service
        location and is used during charge creation to determine the
        type of service.
    """
    class Meta:
        name = "ServiceDeliveryPoint"
        target_namespace = "http://naesb.org/espi"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    tariff_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "tariffProfile",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    customer_agreement: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAgreement",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )


@dataclass
class ServiceStatus(Object1):
    """
    Contains the current status of the service.

    :ivar current_status: The current status of the service.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    current_status: Optional[Union[int, EspiserviceStatusValue]] = field(
        default=None,
        metadata={
            "name": "currentStatus",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SummaryMeasurement(Object1):
    """
    An aggregated summary measurement reading.

    :ivar power_of_ten_multiplier: The multiplier part of the unit of
        measure, e.g. "kilo" (k)
    :ivar time_stamp: The date and time (if needed) of the summary
        measurement.
    :ivar uom: The units of the reading, e.g. "Wh"
    :ivar value: The value of the summary measurement.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = field(
        default=None,
        metadata={
            "name": "powerOfTenMultiplier",
            "type": "Element",
        }
    )
    time_stamp: Optional[int] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
        }
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass
class ReplayProtectType:
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"

    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )
    nonce: Optional[NonceValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )


@dataclass
class BaseUnitType(ItemBaseType):
    """
    Custom Units.
    """
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
    class Meta:
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrLoadControlStateType:
    class Meta:
        name = "oadrLoadControlStateType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrRequestEventType:
    class Meta:
        name = "oadrRequestEventType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Object(ObjectType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureProperty(SignaturePropertyType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureValue(SignatureValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transform(TransformType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class X509DataType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    x509_issuer_serial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    x509_ski: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509SKI",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_subject_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "X509SubjectName",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
        }
    )
    x509_certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    x509_crl: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509CRL",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "sequential": True,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )


@dataclass
class PersonType:
    """
    The Atom person construct is defined in section 3.2 of the format spec.
    """
    class Meta:
        name = "personType"
        target_namespace = "http://www.w3.org/2005/Atom"

    name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    uri: List[UriType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "pattern": r"\w+@(\w+\.)+\w+",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class TextType:
    """
    The Atom text construct is defined in section 3.1 of the format spec.
    """
    class Meta:
        name = "textType"
        target_namespace = "http://www.w3.org/2005/Atom"

    type: Optional[TextTypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class DerencodedKeyValue(DerencodedKeyValueType):
    class Meta:
        name = "DEREncodedKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class GnB(CharTwoFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class KeyInfoReference(KeyInfoReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "PnBFieldParamsType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    k1: Optional[int] = field(
        default=None,
        metadata={
            "name": "K1",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k2: Optional[int] = field(
        default=None,
        metadata={
            "name": "K2",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k3: Optional[int] = field(
        default=None,
        metadata={
            "name": "K3",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class Prime(PrimeFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "TnBFieldParamsType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    k: Optional[int] = field(
        default=None,
        metadata={
            "name": "K",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class X509Digest(X509DigestType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class Duration(DurationPropType):
    """
    The duration of the  activity, data, or state.
    """
    class Meta:
        name = "duration"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Granularity(DurationPropType):
    class Meta:
        name = "granularity"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Iso3AlphaCurrencyCode:
    class Meta:
        name = "ISO3AlphaCurrencyCode"
        namespace = "urn:un:unece:uncefact:codelist:standard:5:ISO42173A:2010-04-07"

    value: Optional[Iso3AlphaCurrencyCodeContentType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EnergyApparentType(EnergyItemType):
    """
    Apparent Energy, measured in volt-ampere hours (VAh)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="ApparentEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class EnergyReactiveType(EnergyItemType):
    """
    Reactive Energy, volt-amperes reactive hours (VARh)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="ReactiveEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VARh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class EnergyRealType(EnergyItemType):
    """
    Real Energy, Watt Hours (Wh)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="RealEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="Wh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class PowerItemType(ItemBaseType):
    """
    Base for the measurement of Power.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
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
    power_attributes: Optional[PowerAttributes] = field(
        default=None,
        metadata={
            "name": "powerAttributes",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class EnergyItem(EnergyItemType):
    class Meta:
        name = "energyItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceLocation(ServiceLocationType):
    class Meta:
        name = "serviceLocation"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Voltage(VoltageType):
    class Meta:
        name = "voltage"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceArea(ServiceAreaType):
    class Meta:
        name = "serviceArea"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"


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
class Responses(ArrayofResponses):
    class Meta:
        name = "responses"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class IdentifiedObject(Object1):
    """
    This is a root class to provide common naming attributes for all classes
    needing naming attributes.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    batch_item_info: Optional[BatchItemInfo] = field(
        default=None,
        metadata={
            "name": "batchItemInfo",
            "type": "Element",
        }
    )


@dataclass
class IntervalReading(Object1):
    """Specific value measured by a meter or other asset.

    Each Reading is associated with a specific ReadingType.

    :ivar cost: [correction] Specifies a cost associated with this
        reading, in hundred-thousandths of the currency specified in the
        ReadingType for this reading. (e.g., 840 = USD, US dollar)
    :ivar reading_quality:
    :ivar time_period: The date time and duration of a reading. If not
        specified, readings for each "intervalLength" in ReadingType are
        present.
    :ivar value: [correction] Value in units specified by ReadingType
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    cost: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    reading_quality: List[ReadingQuality] = field(
        default_factory=list,
        metadata={
            "name": "ReadingQuality",
            "type": "Element",
        }
    )
    time_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timePeriod",
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass
class ReplayProtect(ReplayProtectType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


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
class OadrCanceledOptType:
    class Meta:
        name = "oadrCanceledOptType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrCanceledReportType:
    class Meta:
        name = "oadrCanceledReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrCreatePartyRegistration(OadrCreatePartyRegistrationType):
    """
    Used by VEN to initiate registration with VTN.
    """
    class Meta:
        name = "oadrCreatePartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedOptType:
    class Meta:
        name = "oadrCreatedOptType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrResponseType:
    class Meta:
        name = "oadrResponseType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class KeyValueType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class SignaturePropertiesType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signature_property: List[SignatureProperty] = field(
        default_factory=list,
        metadata={
            "name": "SignatureProperty",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class TransformsType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )


@dataclass
class X509Data(X509DataType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class EntryType:
    """
    The Atom entry construct is defined in section 4.1.2 of the format spec.
    """
    class Meta:
        name = "entryType"
        target_namespace = "http://www.w3.org/2005/Atom"

    author: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    content: List[ContentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    id: List[IdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    published: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    rights: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    source: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    summary: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    updated: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class SourceType:
    """
    The Atom source construct is defined in section 4.2.11 of the format spec.
    """
    class Meta:
        name = "sourceType"
        target_namespace = "http://www.w3.org/2005/Atom"

    author: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    generator: List[GeneratorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    icon: List[IconType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    id: List[IdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    logo: List[LogoType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    rights: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    subtitle: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    updated: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class PnB(PnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnB(TnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class Properties:
    """
    :ivar dtstart:
    :ivar duration:
    :ivar tolerance: Set randomization period for start of event
    :ivar x_ei_notification:
    :ivar x_ei_ramp_up:
    :ivar x_ei_recovery:
    """
    class Meta:
        name = "properties"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tolerance: Optional["Properties.Tolerance"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    x_ei_notification: Optional[XEiNotification] = field(
        default=None,
        metadata={
            "name": "x-eiNotification",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    x_ei_ramp_up: Optional[XEiRampUp] = field(
        default=None,
        metadata={
            "name": "x-eiRampUp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    x_ei_recovery: Optional[XEiRecovery] = field(
        default=None,
        metadata={
            "name": "x-eiRecovery",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )

    @dataclass
    class Tolerance:
        tolerate: Optional["Properties.Tolerance.Tolerate"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class Tolerate:
            startafter: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
                }
            )


@dataclass
class PowerApparentType(PowerItemType):
    """
    Apparent Power measured in volt-amperes (VA)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="ApparentPower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VA",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class PowerReactiveType(PowerItemType):
    """
    Reactive power, measured in volt-amperes reactive (VAR)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="ReactivePower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAR",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class PowerRealType(PowerItemType):
    """
    Real power measured in Watts (W) or Joules/second (J/s)
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    item_description: str = field(
        init=False,
        default="RealPower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass
class EnergyApparent(EnergyApparentType):
    class Meta:
        name = "energyApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyReactive(EnergyReactiveType):
    class Meta:
        name = "energyReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EnergyReal(EnergyRealType):
    class Meta:
        name = "energyReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerItem(PowerItemType):
    class Meta:
        name = "powerItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EiCreatedEvent:
    """
    Respond to a DR Event with optIn or optOut.
    """
    class Meta:
        name = "eiCreatedEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    ei_response: Optional[EiResponse] = field(
        default=None,
        metadata={
            "name": "eiResponse",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    event_responses: Optional[EventResponses] = field(
        default=None,
        metadata={
            "name": "eventResponses",
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
            "required": True,
        }
    )


@dataclass
class EiTargetType:
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class CurrentValueType:
    class Meta:
        name = "currentValueType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    payload_float: Optional[PayloadFloat] = field(
        default=None,
        metadata={
            "name": "payloadFloat",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )


@dataclass
class EiActivePeriodType:
    class Meta:
        name = "eiActivePeriodType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class ElectricPowerQualitySummary(IdentifiedObject):
    """A summary of power quality events.

    This information represents a summary of power quality information
    typically required by customer facility energy management systems.
    It is not intended to satisfy the detailed requirements of power
    quality monitoring. All values are as defined by measurementProtocol
    during the period. The standards typically also give ranges of
    allowed values; the information attributes are the raw measurements,
    not the "yes/no" determination by the various standards. See
    referenced standards for definition, measurement protocol and
    period.

    :ivar flicker_plt: A measurement of long term Rapid Voltage Change
        in hundredths of a Volt. flickerPlt is derived from 2 hours of
        Pst values (12 values combined in cubic relationship).
    :ivar flicker_pst: flickerPst is a value measured over 10 minutes
        that characterizes the likelihood that the voltage fluctuations
        would result in perceptible light flicker. A value of 1.0 is
        designed to represent the level that 50% of people would
        perceive flicker in a 60 watt incandescent bulb. The value
        reported is represented as an integer in hundredths.
    :ivar harmonic_voltage: A measurement of the Harmonic Voltage during
        the period. For DC, distortion is with respect to a signal of
        zero Hz.
    :ivar long_interruptions: A count of Long Interruption events (as
        defined by measurementProtocol) during the summary interval
        period.
    :ivar mains_voltage: A measurement of the Mains [Signaling] Voltage
        during the summary interval period in uV.
    :ivar measurement_protocol: A reference to the source standard used
        as the measurement protocol definition. Examples are: 0 =
        "IEEE1519-2009" 1 = "EN50160"
    :ivar power_frequency: A measurement of the power frequency during
        the summary interval period in uHz.
    :ivar rapid_voltage_changes: A count of Rapid Voltage Change events
        during the summary interval period
    :ivar short_interruptions: A count of Short Interruption events
        during the summary interval period
    :ivar summary_interval: Interval of summary period
    :ivar supply_voltage_dips: A count of Supply Voltage Dip events
        during the summary interval period
    :ivar supply_voltage_imbalance: A count of Supply Voltage Imbalance
        events during the summary interval period
    :ivar supply_voltage_variations: A count of Supply Voltage
        Variations during the summary interval period
    :ivar temp_overvoltage: A count of Temporary Overvoltage events (as
        defined by measurementProtocol) during the summary interval
        period
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    flicker_plt: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPlt",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    flicker_pst: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPst",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    harmonic_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "harmonicVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    long_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "longInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    mains_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "mainsVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    measurement_protocol: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementProtocol",
            "type": "Element",
        }
    )
    power_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "powerFrequency",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    rapid_voltage_changes: Optional[int] = field(
        default=None,
        metadata={
            "name": "rapidVoltageChanges",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    short_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    summary_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "summaryInterval",
            "type": "Element",
            "required": True,
        }
    )
    supply_voltage_dips: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageDips",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    supply_voltage_imbalance: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageImbalance",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    supply_voltage_variations: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageVariations",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    temp_overvoltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "tempOvervoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass
class ElectricPowerUsageSummary(IdentifiedObject):
    """
    Summary of usage for a billing period.

    :ivar billing_period: The billing period to which the included
        measurements apply
    :ivar bill_last_period: The amount of the bill for the previous
        billing period , in hundred-thousandths of the currency
        specified in the ReadingType for this reading (e.g., 840 = USD,
        US dollar).
    :ivar bill_to_date: The bill amount related to the billing period as
        of the date received, in hundred-thousandths of the currency
        specified in the ReadingType for this reading. (e.g., 840 = USD,
        US dollar).
    :ivar cost_additional_last_period: Additional charges from the last
        billing period, in hundred-thousandths of the currency specified
        in the ReadingType for this reading. (e.g., 840 = USD, US
        dollar).
    :ivar cost_additional_detail_last_period: [extension] Additional
        charges from the last billing period which in total add up to
        costAdditionalLastPeriod
    :ivar currency: The ISO 4217 code indicating the currency applicable
        to the bill amounts in the summary. See list at
        http://tiny.cc/4217
    :ivar overall_consumption_last_period: [extension] The amount of
        energy consumed in the last billing period.
    :ivar current_billing_period_over_all_consumption: The total
        consumption for the billing period
    :ivar current_day_last_year_net_consumption: The amount of energy
        consumed one year ago interpreted as same day of week same week
        of year (see ISO 8601).
    :ivar current_day_net_consumption: Net consumption for the current
        day (delivered - received)
    :ivar current_day_overall_consumption: Overall energy consumption
        for the current day
    :ivar peak_demand: Peak demand recorded for the current period
    :ivar previous_day_last_year_overall_consumption: The amount of
        energy consumed on the previous day one year ago interpreted as
        same day of week same week of year (see ISO 8601).
    :ivar previous_day_net_consumption: Net consumption for the previous
        day
    :ivar previous_day_overall_consumption: The total consumption for
        the previous day
    :ivar quality_of_reading: Indication of the quality of the summary
        readings
    :ivar ratchet_demand: The current ratchet demand value for the
        ratchet demand period
    :ivar ratchet_demand_period: The period over which the ratchet
        demand applies
    :ivar status_time_stamp: Date/Time status of this UsageSummary
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    billing_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "billingPeriod",
            "type": "Element",
        }
    )
    bill_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "billLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    bill_to_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "billToDate",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    cost_additional_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "costAdditionalLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    cost_additional_detail_last_period: List[LineItem] = field(
        default_factory=list,
        metadata={
            "name": "costAdditionalDetailLastPeriod",
            "type": "Element",
        }
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    overall_consumption_last_period: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "overallConsumptionLastPeriod",
            "type": "Element",
        }
    )
    current_billing_period_over_all_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentBillingPeriodOverAllConsumption",
            "type": "Element",
        }
    )
    current_day_last_year_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayLastYearNetConsumption",
            "type": "Element",
        }
    )
    current_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayNetConsumption",
            "type": "Element",
        }
    )
    current_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayOverallConsumption",
            "type": "Element",
        }
    )
    peak_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "peakDemand",
            "type": "Element",
        }
    )
    previous_day_last_year_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayLastYearOverallConsumption",
            "type": "Element",
        }
    )
    previous_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayNetConsumption",
            "type": "Element",
        }
    )
    previous_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayOverallConsumption",
            "type": "Element",
        }
    )
    quality_of_reading: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "qualityOfReading",
            "type": "Element",
        }
    )
    ratchet_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratchetDemand",
            "type": "Element",
        }
    )
    ratchet_demand_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "ratchetDemandPeriod",
            "type": "Element",
        }
    )
    status_time_stamp: Optional[int] = field(
        default=None,
        metadata={
            "name": "statusTimeStamp",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class IntervalBlock(IdentifiedObject):
    """
    Time sequence of Readings of the same ReadingType.

    :ivar interval: Specifies the time period during which the contained
        readings were taken.
    :ivar interval_reading:
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    interval_reading: List[IntervalReading] = field(
        default_factory=list,
        metadata={
            "name": "IntervalReading",
            "type": "Element",
        }
    )


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.
    """
    class Meta:
        namespace = "http://naesb.org/espi"


@dataclass
class ReadingType1(IdentifiedObject):
    """
    Characteristics associated with all Readings included in a MeterReading.

    :ivar accumulation_behaviour: Code indicating how value is
        accumulated over time for Readings of ReadingType.
    :ivar commodity: Code for commodity classification of Readings of
        ReadingType.
    :ivar consumption_tier: Code for consumption tier associated with a
        Reading of ReadingType.
    :ivar currency: Code for the currency for costs associated with this
        ReadingType.  The valid values per the standard are defined in
        CurrencyCode.
    :ivar data_qualifier: Code describing a salient attribute of
        Readings of ReadingType.
    :ivar default_quality: Default value to be used if no value of
        ReadingQuality.quality is provided. Specific format and valid
        values per the standard are specified in QualityOfReading.
    :ivar flow_direction: Direction associated with current related
        Readings.
    :ivar interval_length: Default interval length specified in seconds
        for Readings of ReadingType.
    :ivar kind: Code for general classification of a Reading of
        ReadingType.
    :ivar phase: Code for phase information associated with Readings of
        ReadingType.
    :ivar power_of_ten_multiplier: Code for the power of ten multiplier
        which, when used in combination with the uom, specifies the
        actual unit of measure for Readings of ReadingType.
    :ivar time_attribute: Code used to specify a particular type of time
        interval method for Readings of ReadingType.
    :ivar tou: Code for the TOU type of Readings of ReadingType.
    :ivar uom: Code for the base unit of measure for Readings of
        ReadingType.  Used in combination with the powerOfTenMultiplier
        to specify the actual unit of measure
    :ivar cpp: [extension] Critical peak period (CPP) bucket the reading
        value is attributed to. Value 0 means not applicable. Even
        though CPP is usually considered a specialized form of time of
        use 'tou', this attribute is defined explicitly for flexibility.
    :ivar interharmonic: [extension] Indication of a "harmonic" or
        "interharmonic" basis for the measurement. Value 0 in
        'numerator' and 'denominator' means not applicable.
    :ivar measuring_period: [extension] Time attribute inherent or
        fundamental to the reading value (as opposed to 'macroPeriod'
        that supplies an "adjective" to describe aspects of a time
        period with regard to the measurement). It refers to the way the
        value was originally measured and not to the frequency at which
        it is reported or presented. For example, an hourly interval of
        consumption data would have value 'hourly' as an attribute.
        However in the case of an hourly sampled voltage value, the
        meterReadings schema would carry the 'hourly' interval size
        information. It is common for meters to report demand in a form
        that is measured over the course of a portion of an hour, while
        enterprise applications however commonly assume the demand (in
        kW or kVAr) normalised to 1 hour. The sytem that receives
        readings directly from the meter therefore must perform this
        transformation before publishing readings for use by the other
        enterprise systems. The scalar used is chosen based on the block
        size (not any sub-interval size).
    :ivar argument: [extension] Argument used to introduce numbers into
        the unit of measure description where they are needed (e.g., 4
        where the measure needs an argument such as CEMI(n=4)). Most
        arguments used in practice however will be integers (i.e.,
        'denominator'=1). Value 0 in 'numerator' and 'denominator' means
        not applicable.
    """
    class Meta:
        name = "ReadingType"
        namespace = "http://naesb.org/espi"

    accumulation_behaviour: Optional[Union[int, AccumulationKindValue]] = field(
        default=None,
        metadata={
            "name": "accumulationBehaviour",
            "type": "Element",
        }
    )
    commodity: Optional[Union[int, CommodityKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    consumption_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "consumptionTier",
            "type": "Element",
        }
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    data_qualifier: Optional[Union[int, DataQualifierKindValue]] = field(
        default=None,
        metadata={
            "name": "dataQualifier",
            "type": "Element",
        }
    )
    default_quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "defaultQuality",
            "type": "Element",
        }
    )
    flow_direction: Optional[Union[int, FlowDirectionKindValue]] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
        }
    )
    interval_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "intervalLength",
            "type": "Element",
        }
    )
    kind: Optional[Union[int, MeasurementKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    phase: Optional[Union[int, PhaseCodeKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = field(
        default=None,
        metadata={
            "name": "powerOfTenMultiplier",
            "type": "Element",
        }
    )
    time_attribute: Optional[Union[int, TimePeriodOfInterestValue]] = field(
        default=None,
        metadata={
            "name": "timeAttribute",
            "type": "Element",
        }
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    interharmonic: Optional[ReadingInterharmonic] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    measuring_period: Optional[Union[int, TimeAttributeKindValue]] = field(
        default=None,
        metadata={
            "name": "measuringPeriod",
            "type": "Element",
        }
    )
    argument: Optional[RationalNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TimeConfiguration(IdentifiedObject):
    """
    [extension] Contains attributes related to the configuration of the time
    service.

    :ivar dst_end_rule: Rule to calculate end of daylight savings time
        in the current year.  Result of dstEndRule must be greater than
        result of dstStartRule.
    :ivar dst_offset: Daylight savings time offset from local standard
        time.
    :ivar dst_start_rule: Rule to calculate start of daylight savings
        time in the current year. Result of dstEndRule must be greater
        than result of dstStartRule.
    :ivar tz_offset: Local time zone offset from UTCTime. Does not
        include any daylight savings time offsets.
    """
    class Meta:
        target_namespace = "http://naesb.org/espi"

    dst_end_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstEndRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    dst_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "dstOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    dst_start_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstStartRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    tz_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "tzOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


@dataclass
class UsagePoint(IdentifiedObject):
    """
    Logical point on a network at which consumption or production is either
    physically measured (e.g., metered) or estimated (e.g., unmetered street
    lights).

    :ivar role_flags: Specifies the roles that this usage point has been
        assigned. Bit 1 - isMirror Bit 2 - isPremisesAggregationPoint
        Bit 3 - isPEV Bit 4 - isDER Bit 5 - isRevenueQuality Bit 6 -
        isDC Bit 7-16 - Reserved
    :ivar service_category:
    :ivar status: Specifies the current status of this usage point.
        Valid values include: 0 = off 1 = on
    :ivar service_delivery_point: [extension] Contains service delivery
        point information about the UsagePoint if it does represent the
        service delivery point.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    role_flags: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "roleFlags",
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    service_delivery_point: Optional[ServiceDeliveryPoint1] = field(
        default=None,
        metadata={
            "name": "ServiceDeliveryPoint",
            "type": "Element",
        }
    )


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
class OadrCanceledReport(OadrCanceledReportType):
    class Meta:
        name = "oadrCanceledReport"
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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrResponse(OadrResponseType):
    class Meta:
        name = "oadrResponse"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdatedReportType:
    class Meta:
        name = "oadrUpdatedReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class KeyValue(KeyValueType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureProperties(SignaturePropertiesType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Transforms(TransformsType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Entry(EntryType):
    class Meta:
        name = "entry"
        namespace = "http://www.w3.org/2005/Atom"


@dataclass
class FeedType:
    """
    The Atom feed construct is defined in section 4.1.1 of the format spec.
    """
    class Meta:
        name = "feedType"
        target_namespace = "http://www.w3.org/2005/Atom"

    author: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    contributor: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    generator: List[GeneratorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    icon: List[IconType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    id: List[IdType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    logo: List[LogoType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    rights: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    subtitle: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    updated: List[DateTimeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    entry: List[EntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "min_occurs": 3,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "min_occurs": 3,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class FieldIdtype:
    class Meta:
        name = "FieldIDType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    prime: Optional[Prime] = field(
        default=None,
        metadata={
            "name": "Prime",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    tn_b: Optional[TnB] = field(
        default=None,
        metadata={
            "name": "TnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    pn_b: Optional[PnB] = field(
        default=None,
        metadata={
            "name": "PnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    gn_b: Optional[GnB] = field(
        default=None,
        metadata={
            "name": "GnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class AvailableType:
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class WsCalendarIntervalType:
    """
    An interval takes no sub-components.
    """
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class PowerApparent(PowerApparentType):
    class Meta:
        name = "powerApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerReactive(PowerReactiveType):
    class Meta:
        name = "powerReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class PowerReal(PowerRealType):
    class Meta:
        name = "powerReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class CurrentValue(CurrentValueType):
    """
    The payloadFloat value of the event interval currently executing.
    """
    class Meta:
        name = "currentValue"
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
class EiTarget(EiTargetType):
    """Identifies the resources associated with the logical VEN interface.

    For events, the values specified are the target for the event
    """
    class Meta:
        name = "eiTarget"
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
class LocalTimeParameters(TimeConfiguration):
    class Meta:
        namespace = "http://naesb.org/espi"


@dataclass
class OadrCreatedEventType:
    class Meta:
        name = "oadrCreatedEventType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrCreatedPartyRegistration(OadrCreatedPartyRegistrationType):
    """
    Acknowledge receipt of VEN registration, provide VTN registration info.
    """
    class Meta:
        name = "oadrCreatedPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDeviceClass(EiTargetType):
    """Device Class target - use only endDeviceAsset."""
    class Meta:
        name = "oadrDeviceClass"
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
class OadrUpdatedReport(OadrUpdatedReportType):
    """
    Acknowledge receipt of a report.
    """
    class Meta:
        name = "oadrUpdatedReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class ReferenceType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_method: Optional[DigestMethod] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digest_value: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class RetrievalMethodType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class Feed(FeedType):
    class Meta:
        name = "feed"
        namespace = "http://www.w3.org/2005/Atom"


@dataclass
class EcparametersType:
    class Meta:
        name = "ECParametersType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    field_id: Optional[FieldIdtype] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    curve: Optional[CurveType] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    base: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    order: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    co_factor: Optional[int] = field(
        default=None,
        metadata={
            "name": "CoFactor",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    validation_data: Optional[EcvalidationDataType] = field(
        default=None,
        metadata={
            "name": "ValidationData",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )


@dataclass
class Available(AvailableType):
    class Meta:
        name = "available"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Interval1(WsCalendarIntervalType):
    class Meta:
        name = "interval"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


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
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class SignalPayloadType(StreamPayloadBaseType):
    class Meta:
        name = "signalPayloadType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class OadrCreatedEvent(OadrCreatedEventType):
    class Meta:
        name = "oadrCreatedEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbitemBase(ItemBaseType):
    class Meta:
        name = "oadrGBItemBase"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

    feed: Optional[Feed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2005/Atom",
            "required": True,
        }
    )


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class EckeyValueType:
    class Meta:
        name = "ECKeyValueType"
        target_namespace = "http://www.w3.org/2009/xmldsig11#"

    ecparameters: Optional[EcparametersType] = field(
        default=None,
        metadata={
            "name": "ECParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    named_curve: Optional[NamedCurveType] = field(
        default=None,
        metadata={
            "name": "NamedCurve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    public_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PublicKey",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class ArrayOfVavailabilityContainedComponents:
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    available: List[Available] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )


@dataclass
class SignalPayload(SignalPayloadType):
    """
    Signal values for events and baselines.
    """
    class Meta:
        name = "signalPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


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
class OadrReportPayloadType(ReportPayloadType):
    """
    Report payload for use in reports.

    :ivar oadr_data_quality: Enumerated value for the quality of this
        data item
    """
    class Meta:
        name = "oadrReportPayloadType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class KeyInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KeyName",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
                {
                    "name": "MgmtData",
                    "type": str,
                    "namespace": "http://www.w3.org/2000/09/xmldsig#",
                },
            ),
        }
    )


@dataclass
class ManifestType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SignedInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class EckeyValue(EckeyValueType):
    class Meta:
        name = "ECKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class VavailabilityType:
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    components: Optional[ArrayOfVavailabilityContainedComponents] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class SpecifierPayloadType:
    """
    Payload for use in Report Specifiers.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class OadrReportDescriptionType:
    """
    Describes the subject and attributes of a report.
    """
    class Meta:
        name = "oadrReportDescriptionType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrReportPayload(OadrReportPayloadType):
    """
    Data point values for reports.
    """
    class Meta:
        name = "oadrReportPayload"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class KeyInfo(KeyInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignedInfo(SignedInfoType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Vavailability(VavailabilityType):
    """
    A schedule reflecting device availability for participating in DR events.
    """
    class Meta:
        name = "vavailability"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class EiOptType:
    """Opts are used by the VEN to temporarily override the pre-existing
    agreement.

    For example, a VEN may opt in to events during the evening, or opt
    out from events during the world series.
    """
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class IntervalType:
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class SpecifierPayload(SpecifierPayloadType):
    class Meta:
        name = "specifierPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OadrReportDescription(OadrReportDescriptionType):
    class Meta:
        name = "oadrReportDescription"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class SignatureType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signed_info: Optional[SignedInfo] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signature_value: Optional[SignatureValue] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    key_info: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    object_value: List[Object] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
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
    class Meta:
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class Interval2(IntervalType):
    class Meta:
        name = "interval"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OadrCreateOptType(EiOptType):
    class Meta:
        name = "oadrCreateOptType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ReportSpecifier(ReportSpecifierType):
    """
    Specify data points desired in a particular report instance.
    """
    class Meta:
        name = "reportSpecifier"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OadrCreateOpt(OadrCreateOptType):
    """
    Create an optIn or optOut schedule.
    """
    class Meta:
        name = "oadrCreateOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Intervals:
    """
    Time intervals during which the DR event is active or report data is
    available.
    """
    class Meta:
        name = "intervals"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0:stream"

    interval: List[Interval2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "min_occurs": 1,
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
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class OadrReportRequestType:
    """
    This type is used to request an EiReport.
    """
    class Meta:
        name = "oadrReportRequestType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class StreamBaseType:
    """
    abstract base for communication of schedules for signals and observations.
    """
    class Meta:
        target_namespace = "urn:ietf:params:xml:ns:icalendar-2.0:stream"

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
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
        }
    )


@dataclass
class EiEventBaseline(EiEventBaselineType):
    """
    B profile.
    """
    class Meta:
        name = "eiEventBaseline"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignal(EiEventSignalType):
    class Meta:
        name = "eiEventSignal"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OadrReportRequest(OadrReportRequestType):
    class Meta:
        name = "oadrReportRequest"
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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class EiEventSignalsType:
    """
    :ivar ei_event_signal: Interval data for an event
    :ivar ei_event_baseline: Interval data for a baseline
    """
    class Meta:
        name = "eiEventSignalsType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class OadrCreateReportType:
    """
    :ivar request_id:
    :ivar oadr_report_request: Request report
    :ivar ven_id:
    :ivar schema_version:
    """
    class Meta:
        name = "oadrCreateReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrRegisteredReportType:
    class Meta:
        name = "oadrRegisteredReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrReport(OadrReportType):
    class Meta:
        name = "oadrReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class EiEventSignals(EiEventSignalsType):
    """
    Interval data for one or more event signals and/or baselines.
    """
    class Meta:
        name = "eiEventSignals"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OadrCreateReport(OadrCreateReportType):
    """
    Request report from other party.
    """
    class Meta:
        name = "oadrCreateReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRegisterReportType:
    class Meta:
        name = "oadrRegisterReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrRegisteredReport(OadrRegisteredReportType):
    """
    Acknowledge registration of Metadata report by other party.
    """
    class Meta:
        name = "oadrRegisteredReport"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrUpdateReportType:
    class Meta:
        name = "oadrUpdateReportType"
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class EiEventType:
    class Meta:
        name = "eiEventType"
        target_namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

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
class EiEvent(EiEventType):
    class Meta:
        name = "eiEvent"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"


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
        target_namespace = "http://openadr.org/oadr-2.0b/2012/07"

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
class OadrDistributeEvent(OadrDistributeEventType):
    """
    Send DR Events to a VEN.
    """
    class Meta:
        name = "oadrDistributeEvent"
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
