from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2000.pkg_09.xmldsig.pgpdata_type import PgpdataType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "http://www.w3.org/2000/09/xmldsig#"
