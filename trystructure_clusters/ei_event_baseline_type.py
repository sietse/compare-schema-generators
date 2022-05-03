from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_clusters.currency import Currency
from trystructure_clusters.currency_per_kw import CurrencyPerKw
from trystructure_clusters.currency_per_kwh import CurrencyPerKwh
from trystructure_clusters.currency_per_thm import CurrencyPerThm
from trystructure_clusters.current import Current
from trystructure_clusters.custom_unit import CustomUnit
from trystructure_clusters.dtstart import Dtstart
from trystructure_clusters.duration import Duration
from trystructure_clusters.energy_apparent import EnergyApparent
from trystructure_clusters.energy_item import EnergyItem
from trystructure_clusters.energy_reactive import EnergyReactive
from trystructure_clusters.energy_real import EnergyReal
from trystructure_clusters.frequency import Frequency
from trystructure_clusters.intervals import Intervals
from trystructure_clusters.oadr_gbdata_description import OadrGbdataDescription
from trystructure_clusters.power_apparent import PowerApparent
from trystructure_clusters.power_item import PowerItem
from trystructure_clusters.power_reactive import PowerReactive
from trystructure_clusters.power_real import PowerReal
from trystructure_clusters.pulse_count import PulseCount
from trystructure_clusters.temperature import Temperature
from trystructure_clusters.therm import Therm
from trystructure_clusters.voltage import Voltage

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventBaselineType:
    """
    :ivar dtstart:
    :ivar duration:
    :ivar intervals:
    :ivar baseline_id: Unique ID for a specific baseline
    :ivar resource_id:
    :ivar baseline_name: Descriptive name for baseline
    :ivar oadr_gbdata_description:
    :ivar pulse_count:
    :ivar temperature:
    :ivar therm:
    :ivar frequency:
    :ivar currency_per_thm:
    :ivar currency_per_kw:
    :ivar currency_per_kwh:
    :ivar currency:
    :ivar current:
    :ivar custom_unit:
    :ivar power_real:
    :ivar power_reactive:
    :ivar power_apparent:
    :ivar power_item:
    :ivar energy_real:
    :ivar energy_reactive:
    :ivar energy_apparent:
    :ivar energy_item:
    :ivar voltage:
    """
    class Meta:
        name = "eiEventBaselineType"

    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
            "required": True,
        }
    )
    baseline_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "baselineID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "resourceID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    baseline_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "baselineName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    oadr_gbdata_description: Optional[OadrGbdataDescription] = field(
        default=None,
        metadata={
            "name": "oadrGBDataDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    pulse_count: Optional[PulseCount] = field(
        default=None,
        metadata={
            "name": "pulseCount",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    therm: Optional[Therm] = field(
        default=None,
        metadata={
            "name": "Therm",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    frequency: Optional[Frequency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_thm: Optional[CurrencyPerThm] = field(
        default=None,
        metadata={
            "name": "currencyPerThm",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_kw: Optional[CurrencyPerKw] = field(
        default=None,
        metadata={
            "name": "currencyPerKW",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency_per_kwh: Optional[CurrencyPerKwh] = field(
        default=None,
        metadata={
            "name": "currencyPerKWh",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    current: Optional[Current] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    custom_unit: Optional[CustomUnit] = field(
        default=None,
        metadata={
            "name": "customUnit",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
        }
    )
    power_real: Optional[PowerReal] = field(
        default=None,
        metadata={
            "name": "powerReal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_reactive: Optional[PowerReactive] = field(
        default=None,
        metadata={
            "name": "powerReactive",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_apparent: Optional[PowerApparent] = field(
        default=None,
        metadata={
            "name": "powerApparent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    power_item: Optional[PowerItem] = field(
        default=None,
        metadata={
            "name": "powerItem",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_real: Optional[EnergyReal] = field(
        default=None,
        metadata={
            "name": "energyReal",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_reactive: Optional[EnergyReactive] = field(
        default=None,
        metadata={
            "name": "energyReactive",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_apparent: Optional[EnergyApparent] = field(
        default=None,
        metadata={
            "name": "energyApparent",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    energy_item: Optional[EnergyItem] = field(
        default=None,
        metadata={
            "name": "energyItem",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    voltage: Optional[Voltage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
