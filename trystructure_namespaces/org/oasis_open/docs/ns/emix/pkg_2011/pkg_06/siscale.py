from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/siscale"


class SiScaleCodeType(Enum):
    """
    Scale based on representations of SI scale as expressed in the unit
    multipliers enumeration.

    :cvar P: Pico 10**-12
    :cvar N: Nano 10**-9
    :cvar MICRO: Micro 10**-6
    :cvar M: Milli 10**-3
    :cvar C: Centi 10**-2
    :cvar D: Deci 10**-1
    :cvar K: Kilo 10**3
    :cvar M_1: Mega 10**6
    :cvar G: Giga 10**9
    :cvar T: Tera 10**12
    :cvar NONE: Native Scale
    """
    P = "p"
    N = "n"
    MICRO = "micro"
    M = "m"
    C = "c"
    D = "d"
    K = "k"
    M_1 = "M"
    G = "G"
    T = "T"
    NONE = "none"


@dataclass
class SiScaleCode:
    class Meta:
        name = "siScaleCode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/siscale"

    value: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
