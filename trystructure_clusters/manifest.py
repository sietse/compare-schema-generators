from dataclasses import dataclass
from trystructure_clusters.manifest_type import ManifestType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Manifest(ManifestType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
