from dataclasses import dataclass, field
from typing import Optional, Tuple

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, frozen=True)
class FeatureCollection:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    location: Optional["FeatureCollection.Location"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )

    @dataclass(unsafe_hash=True, frozen=True)
    class Location:
        polygon: Optional["FeatureCollection.Location.Polygon"] = field(
            default=None,
            metadata={
                "name": "Polygon",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass(unsafe_hash=True, frozen=True)
        class Polygon:
            exterior: Optional["FeatureCollection.Location.Polygon.Exterior"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.opengis.net/gml/3.2",
                }
            )

            @dataclass(unsafe_hash=True, frozen=True)
            class Exterior:
                linear_ring: Optional["FeatureCollection.Location.Polygon.Exterior.LinearRing"] = field(
                    default=None,
                    metadata={
                        "name": "LinearRing",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass(unsafe_hash=True, frozen=True)
                class LinearRing:
                    pos_list: Tuple[float, ...] = field(
                        default_factory=tuple,
                        metadata={
                            "name": "posList",
                            "type": "Element",
                            "required": True,
                            "tokens": True,
                        }
                    )


@dataclass(unsafe_hash=True, frozen=True)
class PosList:
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Tuple[float, ...] = field(
        default_factory=tuple,
        metadata={
            "tokens": True,
        }
    )
