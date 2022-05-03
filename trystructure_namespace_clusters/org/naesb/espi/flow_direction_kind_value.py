from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


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
