from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
