from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.org.oasis_open.docs.ns.emix.pkg_2011.pkg_06.item_base_type import ItemBaseType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class PulseCountType(ItemBaseType):
    """
    Pulse Count.

    :ivar item_description:
    :ivar item_units: Pulse count from meter
    :ivar pulse_factor:
    """
    class Meta:
        name = "pulseCountType"

    item_description: str = field(
        init=False,
        default="pulse count",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="count",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
    pulse_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "pulseFactor",
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07",
            "required": True,
        }
    )
