from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.current_type import CurrentType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Current(CurrentType):
    class Meta:
        name = "current"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
