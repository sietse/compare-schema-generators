from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_query_registration_type import OadrQueryRegistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrQueryRegistration(OadrQueryRegistrationType):
    """
    Query VTN for registration information without actually registering.
    """
    class Meta:
        name = "oadrQueryRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
