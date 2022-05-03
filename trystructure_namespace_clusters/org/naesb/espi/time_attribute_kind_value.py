from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
