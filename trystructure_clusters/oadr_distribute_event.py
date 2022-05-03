from dataclasses import dataclass
from trystructure_clusters.oadr_distribute_event_type import OadrDistributeEventType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrDistributeEvent(OadrDistributeEventType):
    """
    Send DR Events to a VEN.
    """
    class Meta:
        name = "oadrDistributeEvent"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
