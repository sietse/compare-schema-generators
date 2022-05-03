from dataclasses import dataclass
from trystructure_namespace_clusters.org.naesb.espi.time_configuration import TimeConfiguration

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class LocalTimeParameters(TimeConfiguration):
    class Meta:
        namespace = "http://naesb.org/espi"
