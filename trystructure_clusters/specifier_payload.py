from dataclasses import dataclass
from trystructure_clusters.specifier_payload_type import SpecifierPayloadType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class SpecifierPayload(SpecifierPayloadType):
    class Meta:
        name = "specifierPayload"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
