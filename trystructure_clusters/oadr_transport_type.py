from enum import Enum

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class OadrTransportType(Enum):
    SIMPLE_HTTP = "simpleHttp"
    XMPP = "xmpp"
