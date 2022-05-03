from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


class TimePeriodOfInterestValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_8: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar VALUE_11: Daily Period starting at midnight. If for the
        current day, this specifies the time from midnight to "now".
    :cvar VALUE_13: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar VALUE_22: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar VALUE_24: Weekly period starting at midnight on the first day
        of the week and ending the instant before midnight the last day
        of the week. If within the current week, it specifies the period
        from the start of the week until "now."
    :cvar VALUE_32: For the period defined by the start and end of the
        TimePeriod element in the message.
    """
    VALUE_0 = 0
    VALUE_8 = 8
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_22 = 22
    VALUE_24 = 24
    VALUE_32 = 32
