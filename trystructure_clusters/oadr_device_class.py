from dataclasses import dataclass
from trystructure_clusters.ei_target_type import EiTargetType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDeviceClass(EiTargetType):
    """Device Class target - use only endDeviceAsset."""
    class Meta:
        name = "oadrDeviceClass"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
