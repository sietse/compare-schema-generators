from enum import Enum

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class CurrencyItemDescriptionType(Enum):
    CURRENCY = "currency"
    CURRENCY_PER_KW = "currencyPerKW"
    CURRENCY_PER_KWH = "currencyPerKWh"
