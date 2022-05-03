from dataclasses import dataclass
from trystructure_clusters.oadr_create_party_registration_type import OadrCreatePartyRegistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatePartyRegistration(OadrCreatePartyRegistrationType):
    """
    Used by VEN to initiate registration with VTN.
    """
    class Meta:
        name = "oadrCreatePartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
