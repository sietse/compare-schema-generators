from dataclasses import dataclass
from trystructure_clusters.aggregated_pnode_type import AggregatedPnodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class AggregatedPnode(AggregatedPnodeType):
    class Meta:
        name = "aggregatedPnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
