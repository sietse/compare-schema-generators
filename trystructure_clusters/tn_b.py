from dataclasses import dataclass
from trystructure_clusters.tn_bfield_params_type import TnBfieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnB(TnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
