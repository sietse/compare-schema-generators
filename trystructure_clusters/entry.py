from dataclasses import dataclass
from trystructure_clusters.entry_type import EntryType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class Entry(EntryType):
    class Meta:
        name = "entry"
        namespace = "http://www.w3.org/2005/Atom"
