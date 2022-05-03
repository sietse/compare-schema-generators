from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.power.pnode_type import PnodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Pnode(PnodeType):
    class Meta:
        name = "pnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
