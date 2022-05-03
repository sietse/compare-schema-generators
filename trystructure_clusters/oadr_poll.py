from dataclasses import dataclass
from trystructure_clusters.oadr_poll_type import OadrPollType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPoll(OadrPollType):
    """
    Query pull VTN for payloads with new or modified information.
    """
    class Meta:
        name = "oadrPoll"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
