from dataclasses import dataclass
from trystructure_clusters.prime_field_params_type import PrimeFieldParamsType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class Prime(PrimeFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
