from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.payload_float_type import PayloadFloatType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class PayloadFloat(PayloadFloatType):
    """
    Data point value for event signals or for reporting  current or historical
    values.
    """
    class Meta:
        name = "payloadFloat"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
