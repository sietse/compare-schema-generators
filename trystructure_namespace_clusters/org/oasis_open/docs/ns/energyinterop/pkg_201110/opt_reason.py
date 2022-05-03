from dataclasses import dataclass, field
from typing import Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.opt_reason_enumerated_type import OptReasonEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class OptReason:
    """
    Enumerated value for the opt reason such as x-schedule.
    """
    class Meta:
        name = "optReason"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[OptReasonEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
