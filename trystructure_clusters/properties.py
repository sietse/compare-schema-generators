from dataclasses import dataclass, field
from typing import Optional
from trystructure_clusters.dtstart import Dtstart
from trystructure_clusters.duration import Duration
from trystructure_clusters.x_ei_notification import XEiNotification
from trystructure_clusters.x_ei_ramp_up import XEiRampUp
from trystructure_clusters.x_ei_recovery import XEiRecovery

__NAMESPACE__ = "urn:ietf:params:xml:ns:icalendar-2.0"


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
