from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
