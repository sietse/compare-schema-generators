from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.naesb.espi.date_time_interval import DateTimeInterval
from trystructure_namespace_clusters.org.naesb.espi.identified_object import IdentifiedObject

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
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
