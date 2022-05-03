from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from trystructure_namespace_clusters.org.openadr.oadr_2.pkg_0b.pkg_2012.pkg_07.xmldsig_properties.nonce_value_type import NonceValueType

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties"


@dataclass
class ReplayProtectType:
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )
    nonce: Optional[NonceValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://openadr.org/oadr-2.0b/2012/07/xmldsig-properties",
            "required": True,
        }
    )
