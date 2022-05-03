from dataclasses import dataclass, field
from typing import Optional
from trystructure_namespace_clusters.net.opengis.gml.pkg_3.feature_collection import FeatureCollection

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class ServiceLocationType:
    """A customer ServiceLocation has one or more ServiceDeliveryPoint(s),
    which in turn relate to Meters.

    The location may be a point or a polygon, depending on the specific
    circumstances. For distribution, the ServiceLocation is typically
    the location of the utility customer's premise.
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
