from dataclasses import dataclass
from trystructure_clusters.oadr_gbitem_base import OadrGbitemBase

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrGbdataDescription(OadrGbitemBase):
    class Meta:
        name = "oadrGBDataDescription"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
