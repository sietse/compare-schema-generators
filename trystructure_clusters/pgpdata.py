from dataclasses import dataclass
from trystructure_clusters.pgpdata_type import PgpdataType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
