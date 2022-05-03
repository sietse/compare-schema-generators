from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.xmldsig_properties.replay_protect_type import ReplayProtectType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


@dataclass
class ReplayProtect(ReplayProtectType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"
