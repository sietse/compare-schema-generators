from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.feature_collection import FeatureCollection

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06"


@dataclass
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
