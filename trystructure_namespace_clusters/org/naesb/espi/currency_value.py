from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


class CurrencyValue(Enum):
    """
    :cvar VALUE_840: US dollar
    :cvar VALUE_978: European euro
    :cvar VALUE_36: Australian dollar
    :cvar VALUE_124: Canadian dollar
    :cvar VALUE_756: Swiss francs
    :cvar VALUE_156: Chinese yuan renminbi
    :cvar VALUE_208: Danish crown
    :cvar VALUE_826: British pound
    :cvar VALUE_392: Japanese yen
    :cvar VALUE_578: Norwegian crown
    :cvar VALUE_643: Russian ruble
    :cvar VALUE_752: Swedish crown
    :cvar VALUE_356: India rupees
    :cvar VALUE_0: Another type of currency.
    """
    VALUE_840 = 840
    VALUE_978 = 978
    VALUE_36 = 36
    VALUE_124 = 124
    VALUE_756 = 756
    VALUE_156 = 156
    VALUE_208 = 208
    VALUE_826 = 826
    VALUE_392 = 392
    VALUE_578 = 578
    VALUE_643 = 643
    VALUE_752 = 752
    VALUE_356 = 356
    VALUE_0 = 0
