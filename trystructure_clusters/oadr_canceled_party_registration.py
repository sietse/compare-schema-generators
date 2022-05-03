from dataclasses import dataclass
from trystructure_clusters.oadr_canceled_party_registration_type import OadrCanceledPartyRegistrationType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrCanceledPartyRegistration(OadrCanceledPartyRegistrationType):
    """
    Acknowledge cancelation of registration.
    """
    class Meta:
        name = "oadrCanceledPartyRegistration"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
