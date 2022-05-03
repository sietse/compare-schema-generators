from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.signal_name_enumerated_type import SignalNameEnumeratedType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SignalNameEnumerated:
    class Meta:
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"

    value: Optional[SignalNameEnumeratedType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
