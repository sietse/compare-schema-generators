from dataclasses import dataclass
from trystructure_clusters.oadr_create_opt_type import OadrCreateOptType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreateOpt(OadrCreateOptType):
    """
    Create an optIn or optOut schedule.
    """
    class Meta:
        name = "oadrCreateOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
