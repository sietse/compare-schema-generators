from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.entry_type import EntryType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class Entry(EntryType):
    class Meta:
        name = "entry"
        namespace = "http://www.w3.org/2005/Atom"
