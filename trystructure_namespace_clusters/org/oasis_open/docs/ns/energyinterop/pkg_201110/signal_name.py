from dataclasses import dataclass, field
from typing import Union
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.signal_name_enumerated_type import SignalNameEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalName:
    class Meta:
        name = "signalName"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Union[SignalNameEnumeratedType, str] = field(
        default="",
        metadata={
            "pattern": r"x-\S.*",
        }
    )
