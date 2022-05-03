from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


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
