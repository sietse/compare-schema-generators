from dataclasses import dataclass
from trystructure_clusters.oadr_created_party_registration_type import OadrCreatedPartyRegistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCreatedPartyRegistration(OadrCreatedPartyRegistrationType):
    """
    Acknowledge receipt of VEN registration, provide VTN registration info.
    """
    class Meta:
        name = "oadrCreatedPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
