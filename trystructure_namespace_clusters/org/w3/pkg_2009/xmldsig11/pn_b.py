from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.pn_bfield_params_type import PnBfieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnB(PnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
