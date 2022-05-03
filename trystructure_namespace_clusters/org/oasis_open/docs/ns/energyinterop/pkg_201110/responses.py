from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.arrayof_responses import ArrayofResponses

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class Responses(ArrayofResponses):
    class Meta:
        name = "responses"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
