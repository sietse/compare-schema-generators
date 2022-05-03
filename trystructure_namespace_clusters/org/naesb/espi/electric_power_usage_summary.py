from dataclasses import dataclass, field
from typing import List, Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.currency_value import CurrencyValue
from trystructure_namespace_clusters.org.naesb.espi.date_time_interval import DateTimeInterval
from trystructure_namespace_clusters.org.naesb.espi.identified_object import IdentifiedObject
from trystructure_namespace_clusters.org.naesb.espi.line_item import LineItem
from trystructure_namespace_clusters.org.naesb.espi.quality_of_reading_value import QualityOfReadingValue
from trystructure_namespace_clusters.org.naesb.espi.summary_measurement import SummaryMeasurement

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
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
    cost_additional_detail_last_period: List[LineItem] = field(
        default_factory=list,
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
