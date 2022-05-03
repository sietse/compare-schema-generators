from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.signal_type_enumerated_type import SignalTypeEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalType:
    """
    An enumerated value describing the type of signal such as level or price.
    """
    class Meta:
        name = "signalType"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[SignalTypeEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
