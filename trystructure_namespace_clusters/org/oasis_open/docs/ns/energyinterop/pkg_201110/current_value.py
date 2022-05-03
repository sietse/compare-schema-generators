from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.current_value_type import CurrentValueType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class CurrentValue(CurrentValueType):
    """
    The payloadFloat value of the event interval currently executing.
    """
    class Meta:
        name = "currentValue"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
