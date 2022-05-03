from dataclasses import dataclass
from trystructure_clusters.replay_protect_type import ReplayProtectType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


@dataclass
class ReplayProtect(ReplayProtectType):
    class Meta:
        namespace = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"
