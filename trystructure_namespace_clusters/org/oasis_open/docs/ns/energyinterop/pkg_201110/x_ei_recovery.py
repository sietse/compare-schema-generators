from dataclasses import dataclass
from trystructure_namespace_clusters.ietf.params.xml.ns.icalendar_2.duration_prop_type import DurationPropType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class XEiRecovery(DurationPropType):
    """
    A duration before or after the event end time during which load shed should
    transit.
    """
    class Meta:
        name = "x-eiRecovery"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
