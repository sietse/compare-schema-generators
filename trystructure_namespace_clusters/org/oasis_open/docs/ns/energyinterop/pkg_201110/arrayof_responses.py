from dataclasses import dataclass, field
from typing import List
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.ei_response_type import EiResponseType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ArrayofResponses:
    """Collection of Responses.

    When a service operation regards multiple referenceable items, each
    referenced item may have its own response. Always accompanied by an
    overall Response Type.
    """
    response: List[EiResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
