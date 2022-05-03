from dataclasses import dataclass
from trystructure_clusters.oadr_canceled_opt_type import OadrCanceledOptType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledOpt(OadrCanceledOptType):
    """
    Acknowledge cancelation of an opt schedule.
    """
    class Meta:
        name = "oadrCanceledOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
