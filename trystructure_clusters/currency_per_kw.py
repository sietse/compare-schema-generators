from dataclasses import dataclass
from trystructure_clusters.currency_type import CurrencyType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerKw(CurrencyType):
    class Meta:
        name = "currencyPerKW"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
