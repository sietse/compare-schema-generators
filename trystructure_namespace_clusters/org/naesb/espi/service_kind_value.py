from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
