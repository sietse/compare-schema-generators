from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.opt_reason_enumerated_type import OptReasonEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OptReasonEnumerated:
    class Meta:
        name = "optReasonEnumerated"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[OptReasonEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
