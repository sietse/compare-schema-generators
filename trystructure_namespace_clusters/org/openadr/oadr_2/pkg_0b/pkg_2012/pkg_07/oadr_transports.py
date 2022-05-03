from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.oadr_transport_type import OadrTransportType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


@dataclass
class OadrTransports:
    """
    OpenADR transports supported by implementation.
    """
    class Meta:
        name = "oadrTransports"
        namespace = "http://openadr.org/oadr-2.0b/2012/07"

    oadr_transport: List["OadrTransports.OadrTransport"] = field(
        default_factory=list,
        metadata={
            "name": "oadrTransport",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class OadrTransport:
        oadr_transport_name: Optional[OadrTransportType] = field(
            default=None,
            metadata={
                "name": "oadrTransportName",
                "type": "Element",
                "required": True,
            }
        )
