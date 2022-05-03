from dataclasses import dataclass
from trystructure_clusters.end_device_asset_type import EndDeviceAssetType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class EndDeviceAsset(EndDeviceAssetType):
    class Meta:
        name = "endDeviceAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
