from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


class OptReasonEnumeratedType(Enum):
    """
    Enumerated reasons for opting.
    """
    ECONOMIC = "economic"
    EMERGENCY = "emergency"
    MUST_RUN = "mustRun"
    NOT_PARTICIPATING = "notParticipating"
    OUTAGE_RUN_STATUS = "outageRunStatus"
    OVERRIDE_STATUS = "overrideStatus"
    PARTICIPATING = "participating"
    X_SCHEDULE = "x-schedule"
