from dataclasses import dataclass
from trystructure_clusters.ei_target_type import EiTargetType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportSubject(EiTargetType):
    """Device Class target - use only endDeviceAsset."""
    class Meta:
        name = "reportSubject"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
