from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_request_reregistration_type import OadrRequestReregistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestReregistration(OadrRequestReregistrationType):
    """
    Used by VTN to request that the VEN reregister.
    """
    class Meta:
        name = "oadrRequestReregistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
