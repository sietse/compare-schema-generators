from dataclasses import dataclass
from trystructure_clusters.currency_type import CurrencyType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerThm(CurrencyType):
    class Meta:
        name = "currencyPerThm"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
