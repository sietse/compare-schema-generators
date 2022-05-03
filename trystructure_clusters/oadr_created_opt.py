from dataclasses import dataclass
from trystructure_clusters.oadr_created_opt_type import OadrCreatedOptType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedOpt(OadrCreatedOptType):
    """
    Acknowledge receipt of an opt schedule.
    """
    class Meta:
        name = "oadrCreatedOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
