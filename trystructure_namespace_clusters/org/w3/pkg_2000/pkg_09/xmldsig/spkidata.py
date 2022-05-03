from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.spkidata_type import SpkidataType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
