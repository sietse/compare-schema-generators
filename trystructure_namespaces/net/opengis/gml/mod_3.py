from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
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

    @dataclass
    class Location:
        polygon: Optional["FeatureCollection.Location.Polygon"] = field(
            default=None,
            metadata={
                "name": "Polygon",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
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

            @dataclass
            class Exterior:
                linear_ring: Optional["FeatureCollection.Location.Polygon.Exterior.LinearRing"] = field(
                    default=None,
                    metadata={
                        "name": "LinearRing",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class LinearRing:
                    pos_list: List[float] = field(
                        default_factory=list,
                        metadata={
                            "name": "posList",
                            "type": "Element",
                            "required": True,
                            "tokens": True,
                        }
                    )


@dataclass
class PosList:
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
