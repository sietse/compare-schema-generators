from dataclasses import dataclass
from trystructure_namespace_clusters.org.naesb.espi.identified_object import IdentifiedObject

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.
    """
    class Meta:
        namespace = "http://naesb.org/espi"
