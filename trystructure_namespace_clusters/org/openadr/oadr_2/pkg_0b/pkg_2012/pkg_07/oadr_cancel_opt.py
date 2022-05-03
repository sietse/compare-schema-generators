from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_cancel_opt_type import OadrCancelOptType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelOpt(OadrCancelOptType):
    """
    Cancel an opt schedule.
    """
    class Meta:
        name = "oadrCancelOpt"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
