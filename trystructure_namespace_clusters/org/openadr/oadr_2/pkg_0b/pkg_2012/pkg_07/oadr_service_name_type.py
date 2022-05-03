from enum import Enum

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class OadrServiceNameType(Enum):
    EI_EVENT = "EiEvent"
    EI_OPT = "EiOpt"
    EI_REPORT = "EiReport"
    EI_REGISTER_PARTY = "EiRegisterParty"
    OADR_POLL = "OadrPoll"
