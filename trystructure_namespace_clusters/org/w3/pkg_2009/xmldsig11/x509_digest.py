from dataclasses import dataclass
from trystructure_namespace_clusters.org.w3.pkg_2009.xmldsig11.x509_digest_type import X509DigestType

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class X509Digest(X509DigestType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"
