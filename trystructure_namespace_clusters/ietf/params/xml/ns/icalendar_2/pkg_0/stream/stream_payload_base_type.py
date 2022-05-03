from dataclasses import dataclass

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0:stream"


@dataclass
class StreamPayloadBaseType:
    """Abstract class to convey a payload for a stream.

    When a Stream is transformed to or from a WS-Calendar Interval, the
    contents of the Stream Payload defined element are transformed into
    the contents of a WS-Calendar artifactBase.
    """
