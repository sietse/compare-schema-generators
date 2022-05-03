from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


class UnitSymbolKindValue(Enum):
    """
    :cvar VALUE_61: Apparent power, Volt Ampere (See also real power and
        reactive power.), VA
    :cvar VALUE_38: Real power, Watt. By definition, one Watt equals
        oneJoule per second. Electrical power may have real and reactive
        components. The real portion of electrical power (I²R) or
        VIcos?, is expressed in Watts. (See also apparent power and
        reactive power.), W
    :cvar VALUE_63: Reactive power, Volt Ampere reactive. The “reactive”
        or “imaginary” component of electrical power (VISin?). (See also
        real power and apparent power)., VAr
    :cvar VALUE_71: Apparent energy, Volt Ampere hours, VAh
    :cvar VALUE_72: Real energy, Watt hours, Wh
    :cvar VALUE_73: Reactive energy, Volt Ampere reactive hours, VArh
    :cvar VALUE_29: Electric potential, Volt (W/A), V
    :cvar VALUE_30: Electric resistance, Ohm (V/A), O
    :cvar VALUE_5: Current, ampere, A
    :cvar VALUE_25: Electric capacitance, Farad (C/V), °C
    :cvar VALUE_28: Electric inductance, Henry (Wb/A), H
    :cvar VALUE_23: Relative temperature in degrees Celsius. In the SI
        unit system the symbol is ºC. Electric charge is measured in
        coulomb that has the unit symbol C. To destinguish degree
        Celsius form coulomb the symbol used in the UML is degC. Reason
        for not using ºC is the special character º is difficult to
        manage in software.
    :cvar VALUE_27: Time, seconds, s
    :cvar VALUE_159: Time, minute = s * 60, min
    :cvar VALUE_160: Time, hour = minute * 60, h
    :cvar VALUE_9: Plane angle, degrees, deg
    :cvar VALUE_10: Plane angle, Radian (m/m), rad
    :cvar VALUE_31: Energy joule, (N·m = C·V = W·s), J
    :cvar VALUE_32: Force newton, (kg m/s²), N
    :cvar VALUE_53: Electric conductance, Siemens (A / V = 1 / O), S
    :cvar VALUE_0: N/A, None
    :cvar VALUE_33: Frequency hertz, (1/s), Hz
    :cvar VALUE_3: Mass in gram, g
    :cvar VALUE_39: Pressure, Pascal (N/m²)(Note: the absolute or
        relative measurement of pressure is implied with this entry. See
        below for more explicit forms.), Pa
    :cvar VALUE_2: Length, meter, m
    :cvar VALUE_41: Area, square meter, m²
    :cvar VALUE_42: Volume, cubic meter, m³
    :cvar VALUE_69: Amps squared, amp squared, A2
    :cvar VALUE_105: ampere-squared, Ampere-squared hour, A²h
    :cvar VALUE_70: Amps squared time, square amp second, A²s
    :cvar VALUE_106: Ampere-hours, Ampere-hours, Ah
    :cvar VALUE_152: Current, Ratio of Amperages, A/A
    :cvar VALUE_103: A/m, magnetic field strength, Ampere per metre, A/m
    :cvar VALUE_68: Amp seconds, amp seconds, As
    :cvar VALUE_79: Sound pressure level, Bel, acoustic, Combine with
        multiplier prefix “d” to form decibels of Sound Pressure
        Level“dB (SPL).”, B (SPL)
    :cvar VALUE_113: Signal Strength, Bel-mW, normalized to 1mW. Note:
        to form “dBm” combine “Bm” with multiplier “d”. Bm
    :cvar VALUE_22: Radioactivity, Becquerel (1/s), Bq
    :cvar VALUE_132: Energy, British Thermal Units, BTU
    :cvar VALUE_133: Power, BTU per hour, BTU/h
    :cvar VALUE_8: Luminous intensity, candela, cd
    :cvar VALUE_76: Number of characters, characters, char
    :cvar VALUE_75: Rate of change of frequency, hertz per second, Hz/s
    :cvar VALUE_114: Application Value, encoded value, code
    :cvar VALUE_65: Power factor, Dimensionless <ns1:img
        xmlns:ns1="http://naesb.org/espi" src="HTS_1.PNG" width="64"
        height="29" border="0" alt="graphic"/>, cos?
    :cvar VALUE_111: Amount of substance, counter value, count
    :cvar VALUE_119: Volume, cubic feet, ft³
    :cvar VALUE_120: Volume, cubic feet, ft³(compensated)
    :cvar VALUE_123: Volumetric flow rate, compensated cubic feet per
        hour, ft³(compensated)/h
    :cvar VALUE_78: Turbine inertia, gram·meter2 (Combine with
        multiplier prefix “k” to form kg·m2.), gm²
    :cvar VALUE_144: Concentration, The ratio of the mass of a solute
        divided by the mass of the solution., g/g
    :cvar VALUE_21: Absorbed dose, Gray (J/kg), GY
    :cvar VALUE_150: Frequency, Rate of frequency change, Hz/Hz
    :cvar VALUE_77: Data rate, characters per second, char/s
    :cvar VALUE_130: Volume, imperial gallons, ImperialGal
    :cvar VALUE_131: Volumetric flow rate, Imperial gallons per hour,
        ImperialGal/h
    :cvar VALUE_51: Heat capacity, Joule/Kelvin, J/K
    :cvar VALUE_165: Specific energy, Joules / kg, J/kg
    :cvar VALUE_6: Temperature, Kelvin, K
    :cvar VALUE_158: Catalytic activity, katal = mol / s, kat
    :cvar VALUE_47: Moment of mass ,kilogram meter (kg·m), M
    :cvar VALUE_48: Density, gram/cubic meter (combine with prefix
        multiplier “k” to form kg/ m³), g/m³
    :cvar VALUE_134: Volume, litre = dm3 = m3/1000., L
    :cvar VALUE_157: Volume, litre, with the value compensated for
        weather effects, L(compensated)
    :cvar VALUE_138: Volumetric flow rate, litres (compensated) per
        hour, L(compensated)/h
    :cvar VALUE_137: Volumetric flow rate, litres per hour, L/h
    :cvar VALUE_143: Concentration, The ratio of the volume of a solute
        divided by the volume of the solution., L/L
    :cvar VALUE_82: Volumetric flow rate, Volumetric flow rate, L/s
    :cvar VALUE_156: Volume, litre, with the value uncompensated for
        weather effects., L(uncompensated)
    :cvar VALUE_139: Volumetric flow rate, litres (uncompensated) per
        hour, L(uncompensated)/h
    :cvar VALUE_35: Luminous flux, lumen (cd sr), Lm
    :cvar VALUE_34: Illuminance lux, (lm/m²), L(uncompensated)/h
    :cvar VALUE_49: Viscosity, meter squared / second, m²/s
    :cvar VALUE_167: Volume, cubic meter, with the value compensated for
        weather effects., m3(compensated)
    :cvar VALUE_126: Volumetric flow rate, compensated cubic meters per
        hour, ³(compensated)/h
    :cvar VALUE_125: Volumetric flow rate, cubic meters per hour, m³/h
    :cvar VALUE_45: m3PerSec, cubic meters per second, m³/s
    :cvar VALUE_166: m3uncompensated, cubic meter, with the value
        uncompensated for weather effects., m3(uncompensated)
    :cvar VALUE_127: Volumetric flow rate, uncompensated cubic meters
        per hour, m³(uncompensated)/h
    :cvar VALUE_118: EndDeviceEvent, value to be interpreted as a
        EndDeviceEventCode, meCode
    :cvar VALUE_7: Amount of substance, mole, mol
    :cvar VALUE_147: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms., mol/kg
    :cvar VALUE_145: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in m³., mol/ m³
    :cvar VALUE_146: Concentration, Molar fraction (?), the ratio of the
        molar amount of a solute divided by the molar amount of the
        solution.,mol/mol
    :cvar VALUE_80: Monetary unit, Generic money (Note: Specific
        monetary units are identified the currency class)., ¤
    :cvar VALUE_148: Length, Ratio of length, m/m
    :cvar VALUE_46: Fuel efficiency, meters / cubic meter, m/m³
    :cvar VALUE_43: Velocity, meters per second (m/s), m/s
    :cvar VALUE_44: Acceleration, meters per second squared, m/s²
    :cvar VALUE_102: resistivity, ? (rho), ?m
    :cvar VALUE_155: Pressure, Pascal, absolute pressure, PaA
    :cvar VALUE_140: Pressure, Pascal, gauge pressure, PaG
    :cvar VALUE_141: Pressure, Pounds per square inch, absolute, psiA
    :cvar VALUE_142: Pressure, Pounds per square inch, gauge, psiG
    :cvar VALUE_100: Quantity power, Q, Q
    :cvar VALUE_161: Quantity power, Q measured at 45º, Q45
    :cvar VALUE_163: Quantity energy, Q measured at 45º, Q45h
    :cvar VALUE_162: Quantity power, Q measured at 60º, Q60
    :cvar VALUE_164: Quantity energy, Qh measured at 60º, Q60h
    :cvar VALUE_101: Quantity energy, Qh, Qh
    :cvar VALUE_54: Angular velocity, radians per second, rad/s
    :cvar VALUE_154: Amount of rotation, Revolutions, rev
    :cvar VALUE_4: Rotational speed, Rotations per second, rev/s
    :cvar VALUE_149: Time, Ratio of time (can be combined with an
        multiplier prefix to show rates such as a clock drift rate, e.g.
        “µs/s”), s/s
    :cvar VALUE_11: Solid angle, Steradian (m2/m2), sr
    :cvar VALUE_109: State, "1" = "true", "live", "on", "high", "set";
        "0" = "false", "dead", "off", "low", "cleared"Note: A Boolean
        value is preferred but other values may be supported, status
    :cvar VALUE_24: Doe equivalent, Sievert (J/kg), Sv
    :cvar VALUE_37: Magnetic flux density, Tesla (Wb/m2), T
    :cvar VALUE_169: Energy, Therm, therm
    :cvar VALUE_108: Timestamp, time and date per ISO 8601 format,
        timeStamp
    :cvar VALUE_128: Volume, US gallons, Gal
    :cvar VALUE_129: Volumetric flow rate, US gallons per hour, USGal/h
    :cvar VALUE_67: Volts squared, Volt squared (W2/A2), V²
    :cvar VALUE_104: volt-squared hour, Volt-squared-hours, V²h
    :cvar VALUE_117: Kh-Vah, apparent energy metering constant, VAh/rev
    :cvar VALUE_116: Kh-VArh, reactive energy metering constant,
        VArh/rev
    :cvar VALUE_74: Magnetic flux, Volts per Hertz, V/Hz
    :cvar VALUE_151: Voltage, Ratio of voltages (e.g. mV/V), V/V
    :cvar VALUE_66: Volt seconds, Volt seconds (Ws/A), Vs
    :cvar VALUE_36: Magnetic flux, Weber (V s), Wb
    :cvar VALUE_107: Wh/m3, energy per volume, Wh/m³
    :cvar VALUE_115: Kh-Wh, active energy metering constant, Wh/rev
    :cvar VALUE_50: Thermal conductivity, Watt/meter Kelvin, W/m K
    :cvar VALUE_81: Ramp rate, Watts per second, W/s
    :cvar VALUE_153: Power Factor, PF, W/VA
    :cvar VALUE_168: Signal Strength, Ratio of power, W/W
    """
    VALUE_61 = 61
    VALUE_38 = 38
    VALUE_63 = 63
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_5 = 5
    VALUE_25 = 25
    VALUE_28 = 28
    VALUE_23 = 23
    VALUE_27 = 27
    VALUE_159 = 159
    VALUE_160 = 160
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_53 = 53
    VALUE_0 = 0
    VALUE_33 = 33
    VALUE_3 = 3
    VALUE_39 = 39
    VALUE_2 = 2
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_69 = 69
    VALUE_105 = 105
    VALUE_70 = 70
    VALUE_106 = 106
    VALUE_152 = 152
    VALUE_103 = 103
    VALUE_68 = 68
    VALUE_79 = 79
    VALUE_113 = 113
    VALUE_22 = 22
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_8 = 8
    VALUE_76 = 76
    VALUE_75 = 75
    VALUE_114 = 114
    VALUE_65 = 65
    VALUE_111 = 111
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_123 = 123
    VALUE_78 = 78
    VALUE_144 = 144
    VALUE_21 = 21
    VALUE_150 = 150
    VALUE_77 = 77
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_51 = 51
    VALUE_165 = 165
    VALUE_6 = 6
    VALUE_158 = 158
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_134 = 134
    VALUE_157 = 157
    VALUE_138 = 138
    VALUE_137 = 137
    VALUE_143 = 143
    VALUE_82 = 82
    VALUE_156 = 156
    VALUE_139 = 139
    VALUE_35 = 35
    VALUE_34 = 34
    VALUE_49 = 49
    VALUE_167 = 167
    VALUE_126 = 126
    VALUE_125 = 125
    VALUE_45 = 45
    VALUE_166 = 166
    VALUE_127 = 127
    VALUE_118 = 118
    VALUE_7 = 7
    VALUE_147 = 147
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_80 = 80
    VALUE_148 = 148
    VALUE_46 = 46
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_102 = 102
    VALUE_155 = 155
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_100 = 100
    VALUE_161 = 161
    VALUE_163 = 163
    VALUE_162 = 162
    VALUE_164 = 164
    VALUE_101 = 101
    VALUE_54 = 54
    VALUE_154 = 154
    VALUE_4 = 4
    VALUE_149 = 149
    VALUE_11 = 11
    VALUE_109 = 109
    VALUE_24 = 24
    VALUE_37 = 37
    VALUE_169 = 169
    VALUE_108 = 108
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_67 = 67
    VALUE_104 = 104
    VALUE_117 = 117
    VALUE_116 = 116
    VALUE_74 = 74
    VALUE_151 = 151
    VALUE_66 = 66
    VALUE_36 = 36
    VALUE_107 = 107
    VALUE_115 = 115
    VALUE_50 = 50
    VALUE_81 = 81
    VALUE_153 = 153
    VALUE_168 = 168
