from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
