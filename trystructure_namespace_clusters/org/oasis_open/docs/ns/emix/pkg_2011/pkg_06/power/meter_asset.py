from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.meter_asset_type import MeterAssetType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class MeterAsset(MeterAssetType):
    class Meta:
        name = "meterAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
