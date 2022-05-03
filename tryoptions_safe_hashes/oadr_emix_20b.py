from dataclasses import dataclass, field
from typing import Optional
from tryoptions_safe_hashes.oadr_gml_20b import FeatureCollection

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06"


@dataclass(frozen=True)
class ItemBaseType:
    """
    Abstract base type for units for EMIX Product delivery, measurement, and
    warrants.
    """


@dataclass(frozen=True)
class MarketContext:
    """
    A URI identifying a DR Program.
    """
    class Meta:
        name = "marketContext"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass(frozen=True)
class ServiceAreaType:
    """
    The Service Area is the geographic region that is affected by the EMIX
    market condition.
    """
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass(frozen=True)
class ServiceArea(ServiceAreaType):
    class Meta:
        name = "serviceArea"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06"
