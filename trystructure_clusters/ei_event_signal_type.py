from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_clusters.currency import Currency
from trystructure_clusters.currency_per_kw import CurrencyPerKw
from trystructure_clusters.currency_per_kwh import CurrencyPerKwh
from trystructure_clusters.currency_per_thm import CurrencyPerThm
from trystructure_clusters.current import Current
from trystructure_clusters.current_value import CurrentValue
from trystructure_clusters.custom_unit import CustomUnit
from trystructure_clusters.ei_target import EiTarget
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
from trystructure_clusters.signal_name_enumerated_type import SignalNameEnumeratedType
from trystructure_clusters.signal_type_enumerated_type import SignalTypeEnumeratedType
from trystructure_clusters.temperature import Temperature
from trystructure_clusters.therm import Therm
from trystructure_clusters.voltage import Voltage

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiEventSignalType:
    """
    :ivar intervals:
    :ivar ei_target: Optionally identifies the device class associated
        with the signal. Only the endDeviceAsset subelement is used
    :ivar signal_name: Descriptive name for signal.
    :ivar signal_type:
    :ivar signal_id: unique Identifier for a specific event signal
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
    :ivar current_value:
    """
    class Meta:
        name = "eiEventSignalType"

    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0:stream",
            "required": True,
        }
    )
    ei_target: Optional[EiTarget] = field(
        default=None,
        metadata={
            "name": "eiTarget",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    signal_name: Optional[Union[SignalNameEnumeratedType, str]] = field(
        default=None,
        metadata={
            "name": "signalName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
            "pattern": r"x-\S.*",
        }
    )
    signal_type: Optional[SignalTypeEnumeratedType] = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
            "required": True,
        }
    )
    signal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "signalID",
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
    current_value: Optional[CurrentValue] = field(
        default=None,
        metadata={
            "name": "currentValue",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
