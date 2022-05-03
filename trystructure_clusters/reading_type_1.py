from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.accumulation_kind_value import AccumulationKindValue
from trystructure_clusters.commodity_kind_value import CommodityKindValue
from trystructure_clusters.currency_value import CurrencyValue
from trystructure_clusters.data_qualifier_kind_value import DataQualifierKindValue
from trystructure_clusters.flow_direction_kind_value import FlowDirectionKindValue
from trystructure_clusters.identified_object import IdentifiedObject
from trystructure_clusters.measurement_kind_value import MeasurementKindValue
from trystructure_clusters.phase_code_kind_value import PhaseCodeKindValue
from trystructure_clusters.quality_of_reading_value import QualityOfReadingValue
from trystructure_clusters.rational_number import RationalNumber
from trystructure_clusters.reading_interharmonic import ReadingInterharmonic
from trystructure_clusters.time_attribute_kind_value import TimeAttributeKindValue
from trystructure_clusters.time_period_of_interest_value import TimePeriodOfInterestValue
from trystructure_clusters.unit_multiplier_kind_value import UnitMultiplierKindValue
from trystructure_clusters.unit_symbol_kind_value import UnitSymbolKindValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ReadingType1(IdentifiedObject):
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
        name = "ReadingType"
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
