from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.currency_type import CurrencyType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class CurrencyPerKwh(CurrencyType):
    class Meta:
        name = "currencyPerKWh"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
