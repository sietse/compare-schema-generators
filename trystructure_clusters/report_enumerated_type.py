from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


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
