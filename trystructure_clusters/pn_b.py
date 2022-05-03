from dataclasses import dataclass
from trystructure_clusters.pn_bfield_params_type import PnBfieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnB(PnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
