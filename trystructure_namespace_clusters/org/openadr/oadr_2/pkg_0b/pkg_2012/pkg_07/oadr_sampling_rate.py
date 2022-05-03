from dataclasses import dataclass
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_sampling_rate_type import OadrSamplingRateType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrSamplingRate(OadrSamplingRateType):
    """
    Sampling rate for telemetry type data.
    """
    class Meta:
        name = "oadrSamplingRate"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"
