from enum import Enum

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class ResponseRequiredType(Enum):
    """
    Defines what type of response is required.

    :cvar ALWAYS: Always send a response for every event received.
    :cvar NEVER: Never respond.
    """
    ALWAYS = "always"
    NEVER = "never"
