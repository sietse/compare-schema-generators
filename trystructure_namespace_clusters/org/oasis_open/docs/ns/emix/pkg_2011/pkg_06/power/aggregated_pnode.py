from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.aggregated_pnode_type import AggregatedPnodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class AggregatedPnode(AggregatedPnodeType):
    class Meta:
        name = "aggregatedPnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
