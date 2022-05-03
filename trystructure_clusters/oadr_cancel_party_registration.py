from dataclasses import dataclass
from trystructure_clusters.oadr_cancel_party_registration_type import OadrCancelPartyRegistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCancelPartyRegistration(OadrCancelPartyRegistrationType):
    """
    Cancel a registration.
    """
    class Meta:
        name = "oadrCancelPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
