from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Tuple, Union

__NAMESPACE__ = "http://naesb.org/espi"


class AccumulationKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable, or implied by the unit of measure.
    :cvar VALUE_1: A value from a register which represents the bulk
        quantity of a commodity. This quantity is computed as the
        integral of the commodity usage rate. This value is typically
        used as the basis for the dial reading at the meter, and as a
        result, will roll over upon reaching a maximum dial value. Note
        1: With the metering system, the roll-over behaviour typically
        implies a roll-under behavior so that the value presented is
        always a positive value (e.g. unsigned integer or positive
        decimal.) However, when communicating data between enterprise
        applications a negative value might occur in a case such as net
        metering.Note 2: A BulkQuantity refers primarily to the dial
        reading and not the consumption over a specific period of time.
    :cvar VALUE_2: The sum of the previous billing period values and the
        present period value. Note: “ContinuousCumulative” is commonly
        used in conjunction with “demand.” The “ContinuousCumulative
        Demand” would be the cumulative sum of the previous billing
        period maximum demand values (as occurring with each demand
        reset) summed with the present period maximum demand value
        (which has yet to be reset.)
    :cvar VALUE_3: The sum of the previous billing period values. Note:
        “Cumulative” is commonly used in conjunction with “demand.” Each
        demand reset causes the maximum demand value for the present
        billing period (since the last demand reset) to accumulate as an
        accumulative total of all maximum demands. So instead of
        “zeroing” the demand register, a demand reset has the affect of
        adding the present maximum demand to this accumulating total.
    :cvar VALUE_4: The difference between the value at the end of the
        prescribed interval and the beginning of the interval. This is
        used for incremental interval data. Note: One common application
        would be for load profile data, another use might be to report
        the number of events within an interval (such as the number of
        equipment energizations within the specified period of time.)
    :cvar VALUE_6: As if a needle is swung out on the meter face to a
        value to indicate the current value. (Note: An “indicating”
        value is typically measured over hundreds of milliseconds or
        greater, or may imply a “pusher” mechanism to capture a value.
        Compare this to “instantaneous” which is measured over a shorter
        period of time.)
    :cvar VALUE_9: A form of accumulation which is selective with
        respect to time. Note : “Summation” could be considered a
        specialization of “Bulk Quantity” according to the rules of
        inheritance where “Summation” selectively accumulates pulses
        over a timing pattern, and “BulkQuantity” accumulates pulses all
        of the time.
    :cvar VALUE_10: A form of computation which introduces a time delay
        characteristic to the data value
    :cvar VALUE_12: Typically measured over the fastest period of time
        allowed by the definition of the metric (usually milliseconds or
        tens of milliseconds.) (Note: “Instantaneous” was moved to
        attribute #3 in 61968-9Ed2 from attribute #1 in 61968-9Ed1.)
    :cvar VALUE_13: When this description is applied to a metered value,
        it implies that the value is a time-independent cumulative
        quantity much a BulkQuantity, except that it latches upon the
        maximum value upon reaching that value. Any additional
        accumulation (positive or negative) is discarded until a reset
        occurs. Note: A LatchingQuantity may also occur in the downward
        direction – upon reaching a minimum value. The terms “maximum”
        or “minimum” will usually be included as an attribute when this
        type of accumulation behaviour is present.When this description
        is applied to an encoded value (UOM= “Code”), it implies that
        the value has one or more bits which are latching. The condition
        that caused the bit to be set may have long since evaporated.In
        either case, the timestamp that accompanies the value may not
        coincide with the moment the value was initially set.In both
        cases a system will need to perform an operation to clear the
        latched value.
    :cvar VALUE_14: A time-independent cumulative quantity much a
        BulkQuantity or a LatchingQuantity, except that the accumulation
        stops at the maximum or minimum values. When the maximum is
        reached, any additional positive accumulation is discarded, but
        negative accumulation may be accepted (thus lowering the
        counter.) Likewise, when the negative bound is reached, any
        additional negative accumulation is discarded, but positive
        accumulation is accepted (thus increasing the counter.)
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14


class CrudoperationValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


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


class CurrencyValue(Enum):
    """
    :cvar VALUE_840: US dollar
    :cvar VALUE_978: European euro
    :cvar VALUE_36: Australian dollar
    :cvar VALUE_124: Canadian dollar
    :cvar VALUE_756: Swiss francs
    :cvar VALUE_156: Chinese yuan renminbi
    :cvar VALUE_208: Danish crown
    :cvar VALUE_826: British pound
    :cvar VALUE_392: Japanese yen
    :cvar VALUE_578: Norwegian crown
    :cvar VALUE_643: Russian ruble
    :cvar VALUE_752: Swedish crown
    :cvar VALUE_356: India rupees
    :cvar VALUE_0: Another type of currency.
    """
    VALUE_840 = 840
    VALUE_978 = 978
    VALUE_36 = 36
    VALUE_124 = 124
    VALUE_756 = 756
    VALUE_156 = 156
    VALUE_208 = 208
    VALUE_826 = 826
    VALUE_392 = 392
    VALUE_578 = 578
    VALUE_643 = 643
    VALUE_752 = 752
    VALUE_356 = 356
    VALUE_0 = 0


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


class EspiserviceStatusValue(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


class FlowDirectionKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable (N/A)
    :cvar VALUE_1: "Delivered," or "Imported" as defined 61968-2.Forward
        Active Energy is a positive kWh value as one would naturally
        expect to find as energy is supplied by the utility and consumed
        at the service.Forward Reactive Energy is a positive VArh value
        as one would naturally expect to find in the presence of
        inductive loading.In polyphase metering, the forward energy
        register is incremented when the sum of the phase energies is
        greater than zero.
    :cvar VALUE_2: Typically used to describe that a power factor is
        lagging the reference value. Note 1: When used to describe VA,
        “lagging” describes a form of measurement where reactive power
        is considered in all four quadrants, but real power is
        considered only in quadrants I and IV.Note 2: When used to
        describe power factor, the term “Lagging” implies that the PF is
        negative. The term “lagging” in this case takes the place of the
        negative sign. If a signed PF value is to be passed by the data
        producer, then the direction of flow enumeration zero (none)
        should be used in order to avoid the possibility of creating an
        expression that employs a double negative. The data consumer
        should be able to tell from the sign of the data if the PF is
        leading or lagging. This principle is analogous to the concept
        that “Reverse” energy is an implied negative value, and to
        publish a negative reverse value would be ambiguous.Note 3:
        Lagging power factors typically indicate inductive loading.
    :cvar VALUE_3: Typically used to describe that a power factor is
        leading the reference value.Note: Leading power factors
        typically indicate capacitive loading.
    :cvar VALUE_4: |Forward| - |Reverse|, See 61968-2.Note: In some
        systems, the value passed as a “net” value could become
        negative. In other systems the value passed as a “net” value is
        always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar VALUE_5: Reactive positive quadrants. (The term “lagging” is
        preferred.)
    :cvar VALUE_7: Quadrants 1 and 3
    :cvar VALUE_8: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar VALUE_9: Q1 minus Q4
    :cvar VALUE_10: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar VALUE_11: Quadrants 2 and 4
    :cvar VALUE_12: Q2 minus Q3
    :cvar VALUE_13: Reactive negative quadrants. (The term “leading” is
        preferred.)
    :cvar VALUE_14: Q3 minus Q2
    :cvar VALUE_15: Q1 only
    :cvar VALUE_16: Q2 only
    :cvar VALUE_17: Q3 only
    :cvar VALUE_18: Q4 only
    :cvar VALUE_19: Reverse Active Energy is equivalent to "Received,"
        or "Exported" as defined in 61968-2.Reverse Active Energy is a
        positive kWh value as one would expect to find when energy is
        backfed by the service onto the utility network.Reverse Reactive
        Energy is a positive VArh value as one would expect to find in
        the presence of capacitive loading and a leading Power Factor.In
        polyphase metering, the reverse energy register is incremented
        when the sum of the phase energies is less than zero.Note: The
        value passed as a reverse value is always a positive value. It
        is understood by the label “reverse” that it represents negative
        flow.
    :cvar VALUE_20: |Forward| + |Reverse|, See 61968-2.The sum of the
        commodity in all quadrants Q1+Q2+Q3+Q4.In polyphase metering,
        the total energy register is incremented when the absolute value
        of the sum of the phase energies is greater than zero.
    :cvar VALUE_21: In polyphase metering, the total by phase energy
        register is incremented when the sum of the absolute values of
        the phase energies is greater than zero.In single phase
        metering, the formulas for “Total” and “Total by phase” collapse
        to the same expression. For communication purposes however, the
        “Total” enumeration should be used with single phase meter data.
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
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


@dataclass(unsafe_hash=True, frozen=True)
class LineItem:
    """
    [extension] Line item of detail for additional cost.
    """
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    rounding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )


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


@dataclass(unsafe_hash=True, frozen=True)
class Object:
    """
    Superclass of all object classes to allow extensions.

    :ivar extension: Contains an extension.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    extension: Tuple[object, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
        }
    )


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


@dataclass(unsafe_hash=True, frozen=True)
class RationalNumber:
    """[extension] Rational number = 'numerator' / 'denominator'."""
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ReadingInterharmonic:
    """
    [extension] Interharmonics are represented as a rational number 'numerator'
    / 'denominator', and harmonics are represented using the same mechanism and
    identified by 'denominator'=1.
    """
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        }
    )


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


class StatusCodeValue(Enum):
    VALUE_200 = 200
    VALUE_201 = 201
    VALUE_204 = 204
    VALUE_301 = 301
    VALUE_302 = 302
    VALUE_304 = 304
    VALUE_400 = 400
    VALUE_401 = 401
    VALUE_403 = 403
    VALUE_404 = 404
    VALUE_405 = 405
    VALUE_410 = 410
    VALUE_500 = 500


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


class TimePeriodOfInterestValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_8: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar VALUE_11: Daily Period starting at midnight. If for the
        current day, this specifies the time from midnight to "now".
    :cvar VALUE_13: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar VALUE_22: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar VALUE_24: Weekly period starting at midnight on the first day
        of the week and ending the instant before midnight the last day
        of the week. If within the current week, it specifies the period
        from the start of the week until "now."
    :cvar VALUE_32: For the period defined by the start and end of the
        TimePeriod element in the message.
    """
    VALUE_0 = 0
    VALUE_8 = 8
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_22 = 22
    VALUE_24 = 24
    VALUE_32 = 32


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


@dataclass(unsafe_hash=True, frozen=True)
class BatchItemInfo(Object):
    """
    Includes elements that make it possible to include multiple transactions in
    a single (batch) request.

    :ivar name: An identifier for this object that is only unique within
        the containing collection.
    :ivar operation: Specifies the operation requested of this item.
    :ivar status_code: Indicates the status code of the associated
        transaction.
    :ivar status_reason: Indicates the reason for the indicated status
        code.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    name: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    operation: Optional[Union[int, CrudoperationValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    status_code: Optional[Union[int, StatusCodeValue]] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
        }
    )
    status_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusReason",
            "type": "Element",
            "max_length": 256,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class DateTimeInterval(Object):
    """Interval of date and time.

    End is not included because it can be derived from the start and the
    duration.

    :ivar duration: [correction] Duration of the interval, in seconds.
    :ivar start: [correction] Date and time that this interval started.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ReadingQuality(Object):
    """Quality of a specific reading value or interval reading value.

    Note that more than one Quality may be applicable to a given
    Reading. Typically not used unless problems or unusual conditions
    occur (i.e., quality for each Reading is assumed to be 'Good'
    (valid) unless stated otherwise in associated ReadingQuality).

    :ivar quality: Quality, to be specified if different than
        ReadingType.defaultQuality. The specific format is specified per
        the standard is defined in QualityOfReading.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ServiceCategory(Object):
    """
    Category of service provided to the customer.

    :ivar kind: Service classification Examples are: 0 - electricity 1 -
        gas The list of specific valid values per the standard are
        itemized in ServiceKind.
    """
    kind: Optional[Union[int, ServiceKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ServiceDeliveryPoint(Object):
    """
    [extension] Service Delivery Point is representation of revenue UsagePoint
    attributes.

    :ivar name: The name is any free human readable and possibly non
        unique text naming the object.
    :ivar tariff_profile: A schedule of charges; structure associated
        with Tariff that allows the definition of complex tariff
        structures such as step and time of use.
    :ivar customer_agreement: Agreement between the customer and the
        ServiceSupplier to pay for service at a specific service
        location. It provides for the recording of certain billing
        information about the type of service provided at the service
        location and is used during charge creation to determine the
        type of service.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    tariff_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "tariffProfile",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )
    customer_agreement: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAgreement",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ServiceStatus(Object):
    """
    Contains the current status of the service.

    :ivar current_status: The current status of the service.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    current_status: Optional[Union[int, EspiserviceStatusValue]] = field(
        default=None,
        metadata={
            "name": "currentStatus",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class SummaryMeasurement(Object):
    """
    An aggregated summary measurement reading.

    :ivar power_of_ten_multiplier: The multiplier part of the unit of
        measure, e.g. "kilo" (k)
    :ivar time_stamp: The date and time (if needed) of the summary
        measurement.
    :ivar uom: The units of the reading, e.g. "Wh"
    :ivar value: The value of the summary measurement.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = field(
        default=None,
        metadata={
            "name": "powerOfTenMultiplier",
            "type": "Element",
        }
    )
    time_stamp: Optional[int] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
        }
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class IdentifiedObject(Object):
    """
    This is a root class to provide common naming attributes for all classes
    needing naming attributes.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    batch_item_info: Optional[BatchItemInfo] = field(
        default=None,
        metadata={
            "name": "batchItemInfo",
            "type": "Element",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class IntervalReading(Object):
    """Specific value measured by a meter or other asset.

    Each Reading is associated with a specific ReadingType.

    :ivar cost: [correction] Specifies a cost associated with this
        reading, in hundred-thousandths of the currency specified in the
        ReadingType for this reading. (e.g., 840 = USD, US dollar)
    :ivar reading_quality:
    :ivar time_period: The date time and duration of a reading. If not
        specified, readings for each "intervalLength" in ReadingType are
        present.
    :ivar value: [correction] Value in units specified by ReadingType
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    cost: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    reading_quality: Tuple[ReadingQuality, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReadingQuality",
            "type": "Element",
        }
    )
    time_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timePeriod",
            "type": "Element",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ElectricPowerQualitySummary(IdentifiedObject):
    """A summary of power quality events.

    This information represents a summary of power quality information
    typically required by customer facility energy management systems.
    It is not intended to satisfy the detailed requirements of power
    quality monitoring. All values are as defined by measurementProtocol
    during the period. The standards typically also give ranges of
    allowed values; the information attributes are the raw measurements,
    not the "yes/no" determination by the various standards. See
    referenced standards for definition, measurement protocol and
    period.

    :ivar flicker_plt: A measurement of long term Rapid Voltage Change
        in hundredths of a Volt. flickerPlt is derived from 2 hours of
        Pst values (12 values combined in cubic relationship).
    :ivar flicker_pst: flickerPst is a value measured over 10 minutes
        that characterizes the likelihood that the voltage fluctuations
        would result in perceptible light flicker. A value of 1.0 is
        designed to represent the level that 50% of people would
        perceive flicker in a 60 watt incandescent bulb. The value
        reported is represented as an integer in hundredths.
    :ivar harmonic_voltage: A measurement of the Harmonic Voltage during
        the period. For DC, distortion is with respect to a signal of
        zero Hz.
    :ivar long_interruptions: A count of Long Interruption events (as
        defined by measurementProtocol) during the summary interval
        period.
    :ivar mains_voltage: A measurement of the Mains [Signaling] Voltage
        during the summary interval period in uV.
    :ivar measurement_protocol: A reference to the source standard used
        as the measurement protocol definition. Examples are: 0 =
        "IEEE1519-2009" 1 = "EN50160"
    :ivar power_frequency: A measurement of the power frequency during
        the summary interval period in uHz.
    :ivar rapid_voltage_changes: A count of Rapid Voltage Change events
        during the summary interval period
    :ivar short_interruptions: A count of Short Interruption events
        during the summary interval period
    :ivar summary_interval: Interval of summary period
    :ivar supply_voltage_dips: A count of Supply Voltage Dip events
        during the summary interval period
    :ivar supply_voltage_imbalance: A count of Supply Voltage Imbalance
        events during the summary interval period
    :ivar supply_voltage_variations: A count of Supply Voltage
        Variations during the summary interval period
    :ivar temp_overvoltage: A count of Temporary Overvoltage events (as
        defined by measurementProtocol) during the summary interval
        period
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    flicker_plt: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPlt",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    flicker_pst: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPst",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    harmonic_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "harmonicVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    long_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "longInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    mains_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "mainsVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    measurement_protocol: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementProtocol",
            "type": "Element",
        }
    )
    power_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "powerFrequency",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    rapid_voltage_changes: Optional[int] = field(
        default=None,
        metadata={
            "name": "rapidVoltageChanges",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    short_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    summary_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "summaryInterval",
            "type": "Element",
            "required": True,
        }
    )
    supply_voltage_dips: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageDips",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    supply_voltage_imbalance: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageImbalance",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    supply_voltage_variations: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageVariations",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    temp_overvoltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "tempOvervoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ElectricPowerUsageSummary(IdentifiedObject):
    """
    Summary of usage for a billing period.

    :ivar billing_period: The billing period to which the included
        measurements apply
    :ivar bill_last_period: The amount of the bill for the previous
        billing period , in hundred-thousandths of the currency
        specified in the ReadingType for this reading (e.g., 840 = USD,
        US dollar).
    :ivar bill_to_date: The bill amount related to the billing period as
        of the date received, in hundred-thousandths of the currency
        specified in the ReadingType for this reading. (e.g., 840 = USD,
        US dollar).
    :ivar cost_additional_last_period: Additional charges from the last
        billing period, in hundred-thousandths of the currency specified
        in the ReadingType for this reading. (e.g., 840 = USD, US
        dollar).
    :ivar cost_additional_detail_last_period: [extension] Additional
        charges from the last billing period which in total add up to
        costAdditionalLastPeriod
    :ivar currency: The ISO 4217 code indicating the currency applicable
        to the bill amounts in the summary. See list at
        http://tiny.cc/4217
    :ivar overall_consumption_last_period: [extension] The amount of
        energy consumed in the last billing period.
    :ivar current_billing_period_over_all_consumption: The total
        consumption for the billing period
    :ivar current_day_last_year_net_consumption: The amount of energy
        consumed one year ago interpreted as same day of week same week
        of year (see ISO 8601).
    :ivar current_day_net_consumption: Net consumption for the current
        day (delivered - received)
    :ivar current_day_overall_consumption: Overall energy consumption
        for the current day
    :ivar peak_demand: Peak demand recorded for the current period
    :ivar previous_day_last_year_overall_consumption: The amount of
        energy consumed on the previous day one year ago interpreted as
        same day of week same week of year (see ISO 8601).
    :ivar previous_day_net_consumption: Net consumption for the previous
        day
    :ivar previous_day_overall_consumption: The total consumption for
        the previous day
    :ivar quality_of_reading: Indication of the quality of the summary
        readings
    :ivar ratchet_demand: The current ratchet demand value for the
        ratchet demand period
    :ivar ratchet_demand_period: The period over which the ratchet
        demand applies
    :ivar status_time_stamp: Date/Time status of this UsageSummary
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    billing_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "billingPeriod",
            "type": "Element",
        }
    )
    bill_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "billLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    bill_to_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "billToDate",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    cost_additional_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "costAdditionalLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    cost_additional_detail_last_period: Tuple[LineItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "costAdditionalDetailLastPeriod",
            "type": "Element",
        }
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    overall_consumption_last_period: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "overallConsumptionLastPeriod",
            "type": "Element",
        }
    )
    current_billing_period_over_all_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentBillingPeriodOverAllConsumption",
            "type": "Element",
        }
    )
    current_day_last_year_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayLastYearNetConsumption",
            "type": "Element",
        }
    )
    current_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayNetConsumption",
            "type": "Element",
        }
    )
    current_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayOverallConsumption",
            "type": "Element",
        }
    )
    peak_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "peakDemand",
            "type": "Element",
        }
    )
    previous_day_last_year_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayLastYearOverallConsumption",
            "type": "Element",
        }
    )
    previous_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayNetConsumption",
            "type": "Element",
        }
    )
    previous_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayOverallConsumption",
            "type": "Element",
        }
    )
    quality_of_reading: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "qualityOfReading",
            "type": "Element",
        }
    )
    ratchet_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratchetDemand",
            "type": "Element",
        }
    )
    ratchet_demand_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "ratchetDemandPeriod",
            "type": "Element",
        }
    )
    status_time_stamp: Optional[int] = field(
        default=None,
        metadata={
            "name": "statusTimeStamp",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class IntervalBlock(IdentifiedObject):
    """
    Time sequence of Readings of the same ReadingType.

    :ivar interval: Specifies the time period during which the contained
        readings were taken.
    :ivar interval_reading:
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    interval_reading: Tuple[IntervalReading, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "IntervalReading",
            "type": "Element",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.
    """
    class Meta:
        namespace = "http://naesb.org/espi"


@dataclass(unsafe_hash=True, frozen=True)
class ReadingType(IdentifiedObject):
    """
    Characteristics associated with all Readings included in a MeterReading.

    :ivar accumulation_behaviour: Code indicating how value is
        accumulated over time for Readings of ReadingType.
    :ivar commodity: Code for commodity classification of Readings of
        ReadingType.
    :ivar consumption_tier: Code for consumption tier associated with a
        Reading of ReadingType.
    :ivar currency: Code for the currency for costs associated with this
        ReadingType.  The valid values per the standard are defined in
        CurrencyCode.
    :ivar data_qualifier: Code describing a salient attribute of
        Readings of ReadingType.
    :ivar default_quality: Default value to be used if no value of
        ReadingQuality.quality is provided. Specific format and valid
        values per the standard are specified in QualityOfReading.
    :ivar flow_direction: Direction associated with current related
        Readings.
    :ivar interval_length: Default interval length specified in seconds
        for Readings of ReadingType.
    :ivar kind: Code for general classification of a Reading of
        ReadingType.
    :ivar phase: Code for phase information associated with Readings of
        ReadingType.
    :ivar power_of_ten_multiplier: Code for the power of ten multiplier
        which, when used in combination with the uom, specifies the
        actual unit of measure for Readings of ReadingType.
    :ivar time_attribute: Code used to specify a particular type of time
        interval method for Readings of ReadingType.
    :ivar tou: Code for the TOU type of Readings of ReadingType.
    :ivar uom: Code for the base unit of measure for Readings of
        ReadingType.  Used in combination with the powerOfTenMultiplier
        to specify the actual unit of measure
    :ivar cpp: [extension] Critical peak period (CPP) bucket the reading
        value is attributed to. Value 0 means not applicable. Even
        though CPP is usually considered a specialized form of time of
        use 'tou', this attribute is defined explicitly for flexibility.
    :ivar interharmonic: [extension] Indication of a "harmonic" or
        "interharmonic" basis for the measurement. Value 0 in
        'numerator' and 'denominator' means not applicable.
    :ivar measuring_period: [extension] Time attribute inherent or
        fundamental to the reading value (as opposed to 'macroPeriod'
        that supplies an "adjective" to describe aspects of a time
        period with regard to the measurement). It refers to the way the
        value was originally measured and not to the frequency at which
        it is reported or presented. For example, an hourly interval of
        consumption data would have value 'hourly' as an attribute.
        However in the case of an hourly sampled voltage value, the
        meterReadings schema would carry the 'hourly' interval size
        information. It is common for meters to report demand in a form
        that is measured over the course of a portion of an hour, while
        enterprise applications however commonly assume the demand (in
        kW or kVAr) normalised to 1 hour. The sytem that receives
        readings directly from the meter therefore must perform this
        transformation before publishing readings for use by the other
        enterprise systems. The scalar used is chosen based on the block
        size (not any sub-interval size).
    :ivar argument: [extension] Argument used to introduce numbers into
        the unit of measure description where they are needed (e.g., 4
        where the measure needs an argument such as CEMI(n=4)). Most
        arguments used in practice however will be integers (i.e.,
        'denominator'=1). Value 0 in 'numerator' and 'denominator' means
        not applicable.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    accumulation_behaviour: Optional[Union[int, AccumulationKindValue]] = field(
        default=None,
        metadata={
            "name": "accumulationBehaviour",
            "type": "Element",
        }
    )
    commodity: Optional[Union[int, CommodityKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    consumption_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "consumptionTier",
            "type": "Element",
        }
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    data_qualifier: Optional[Union[int, DataQualifierKindValue]] = field(
        default=None,
        metadata={
            "name": "dataQualifier",
            "type": "Element",
        }
    )
    default_quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "defaultQuality",
            "type": "Element",
        }
    )
    flow_direction: Optional[Union[int, FlowDirectionKindValue]] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
        }
    )
    interval_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "intervalLength",
            "type": "Element",
        }
    )
    kind: Optional[Union[int, MeasurementKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    phase: Optional[Union[int, PhaseCodeKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = field(
        default=None,
        metadata={
            "name": "powerOfTenMultiplier",
            "type": "Element",
        }
    )
    time_attribute: Optional[Union[int, TimePeriodOfInterestValue]] = field(
        default=None,
        metadata={
            "name": "timeAttribute",
            "type": "Element",
        }
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    interharmonic: Optional[ReadingInterharmonic] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    measuring_period: Optional[Union[int, TimeAttributeKindValue]] = field(
        default=None,
        metadata={
            "name": "measuringPeriod",
            "type": "Element",
        }
    )
    argument: Optional[RationalNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class TimeConfiguration(IdentifiedObject):
    """
    [extension] Contains attributes related to the configuration of the time
    service.

    :ivar dst_end_rule: Rule to calculate end of daylight savings time
        in the current year.  Result of dstEndRule must be greater than
        result of dstStartRule.
    :ivar dst_offset: Daylight savings time offset from local standard
        time.
    :ivar dst_start_rule: Rule to calculate start of daylight savings
        time in the current year. Result of dstEndRule must be greater
        than result of dstStartRule.
    :ivar tz_offset: Local time zone offset from UTCTime. Does not
        include any daylight savings time offsets.
    """
    dst_end_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstEndRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    dst_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "dstOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    dst_start_rule: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "dstStartRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    tz_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "tzOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class UsagePoint(IdentifiedObject):
    """
    Logical point on a network at which consumption or production is either
    physically measured (e.g., metered) or estimated (e.g., unmetered street
    lights).

    :ivar role_flags: Specifies the roles that this usage point has been
        assigned. Bit 1 - isMirror Bit 2 - isPremisesAggregationPoint
        Bit 3 - isPEV Bit 4 - isDER Bit 5 - isRevenueQuality Bit 6 -
        isDC Bit 7-16 - Reserved
    :ivar service_category:
    :ivar status: Specifies the current status of this usage point.
        Valid values include: 0 = off 1 = on
    :ivar service_delivery_point: [extension] Contains service delivery
        point information about the UsagePoint if it does represent the
        service delivery point.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    role_flags: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "roleFlags",
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        }
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    service_delivery_point: Optional[ServiceDeliveryPoint] = field(
        default=None,
        metadata={
            "name": "ServiceDeliveryPoint",
            "type": "Element",
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class LocalTimeParameters(TimeConfiguration):
    class Meta:
        namespace = "http://naesb.org/espi"
