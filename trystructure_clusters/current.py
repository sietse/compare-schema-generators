from dataclasses import dataclass
from trystructure_clusters.current_type import CurrentType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class Current(CurrentType):
    class Meta:
        name = "current"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
