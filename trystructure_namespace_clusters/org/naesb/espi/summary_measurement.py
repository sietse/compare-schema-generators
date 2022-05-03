from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object
from trystructure_namespace_clusters.org.naesb.espi.unit_multiplier_kind_value import UnitMultiplierKindValue
from trystructure_namespace_clusters.org.naesb.espi.unit_symbol_kind_value import UnitSymbolKindValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
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
