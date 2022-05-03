from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


class EventStatusEnumeratedType(Enum):
    """
    :cvar NONE: No event pending
    :cvar FAR: Event pending in the far future. The exact definition of
        how far in the future this refers is dependent upon the market
        context, but typically means the next day.
    :cvar NEAR: Event pending in the near future. The exact definition
        of how near in the future the pending event is active is
        dependent on the market context.
    :cvar ACTIVE: The event has been initiated and is currently active.
    :cvar COMPLETED: The event has completed.
    :cvar CANCELLED: The event has been canceled.
    """
    NONE = "none"
    FAR = "far"
    NEAR = "near"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
