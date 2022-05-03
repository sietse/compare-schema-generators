from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_poll_type import OadrPollType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrPoll(OadrPollType):
    """
    Query pull VTN for payloads with new or modified information.
    """
    class Meta:
        name = "oadrPoll"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
