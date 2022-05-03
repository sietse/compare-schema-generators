from dataclasses import dataclass
from trystructure_clusters.qualified_event_idtype import QualifiedEventIdtype

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class QualifiedEventId(QualifiedEventIdtype):
    class Meta:
        name = "qualifiedEventID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
