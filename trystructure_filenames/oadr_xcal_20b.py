from dataclasses import dataclass, field
from typing import List, Optional
from trystructure_filenames.oadr_ei_20b import (
    XEiNotification,
    XEiRampUp,
    XEiRecovery,
)

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class DurationPropType:
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
            "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
        }
    )


@dataclass
class Components:
    class Meta:
        name = "components"
        nillable = True
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class DateTime:
    class Meta:
        name = "date-time"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Dtend:
    class Meta:
        name = "dtend"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Dtstart:
    """
    The starting time for the activity, data, or state change.
    """
    class Meta:
        name = "dtstart"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
            "required": True,
            "pattern": r"(\-|\+)?\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}(\.\d*)?Z?",
        }
    )


@dataclass
class Text:
    class Meta:
        name = "text"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Uid:
    """
    Used as an index to identify intervals.
    """
    class Meta:
        name = "uid"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Duration(DurationPropType):
    """
    The duration of the  activity, data, or state.
    """
    class Meta:
        name = "duration"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Granularity(DurationPropType):
    class Meta:
        name = "granularity"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Properties:
    """
    :ivar dtstart:
    :ivar duration:
    :ivar tolerance: Set randomization period for start of event
    :ivar x_ei_notification:
    :ivar x_ei_ramp_up:
    :ivar x_ei_recovery:
    """
    class Meta:
        name = "properties"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"

    dtstart: Optional[Dtstart] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tolerance: Optional["Properties.Tolerance"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    x_ei_notification: Optional[XEiNotification] = field(
        default=None,
        metadata={
            "name": "x-eiNotification",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    x_ei_ramp_up: Optional[XEiRampUp] = field(
        default=None,
        metadata={
            "name": "x-eiRampUp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    x_ei_recovery: Optional[XEiRecovery] = field(
        default=None,
        metadata={
            "name": "x-eiRecovery",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )

    @dataclass
    class Tolerance:
        tolerate: Optional["Properties.Tolerance.Tolerate"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class Tolerate:
            startafter: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "pattern": r"(\+|\-)?P((\d+Y)?(\d+M)?(\d+D)?T?(\d+H)?(\d+M)?(\d+S)?)|(\d+W)",
                }
            )


@dataclass
class AvailableType:
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class WsCalendarIntervalType:
    """
    An interval takes no sub-components.
    """
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class Available(AvailableType):
    class Meta:
        name = "available"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class Interval(WsCalendarIntervalType):
    class Meta:
        name = "interval"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"


@dataclass
class ArrayOfVavailabilityContainedComponents:
    available: List[Available] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
        }
    )


@dataclass
class VavailabilityType:
    components: Optional[ArrayOfVavailabilityContainedComponents] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:ietf:params:xml:ns:icalendar-2.0",
            "required": True,
        }
    )


@dataclass
class Vavailability(VavailabilityType):
    """
    A schedule reflecting device availability for participating in DR events.
    """
    class Meta:
        name = "vavailability"
        namespace = "urn:ietf:params:xml:ns:icalendar-2.0"
