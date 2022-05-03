from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.opt_type_type import OptTypeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OptType:
    """
    optIn or optOut of an event.
    """
    class Meta:
        name = "optType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[OptTypeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
