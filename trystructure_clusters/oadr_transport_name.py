from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.oadr_transport_type import OadrTransportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrTransportName:
    """
    OpenADR transport name such as simpleHttp or xmpp.
    """
    class Meta:
        name = "oadrTransportName"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    value: Optional[OadrTransportType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
