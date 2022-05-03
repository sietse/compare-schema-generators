from dataclasses import dataclass
from trystructure_clusters.duration_prop_type import DurationPropType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrRequestedOadrPollFreq(DurationPropType):
    """
    The VEN shall send an oadrPoll payload to the VTN at most once for each
    duration specified by this element.
    """
    class Meta:
        name = "oadrRequestedOadrPollFreq"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
