from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2005.atom.feed_type import FeedType

__NAMESPACE__ = "http://www.w3.org/2005/Atom"


@dataclass
class Feed(FeedType):
    class Meta:
        name = "feed"
        namespace = "http://www.w3.org/2005/Atom"
