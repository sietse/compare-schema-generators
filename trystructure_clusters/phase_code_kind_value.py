from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
