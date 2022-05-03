from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
