from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
