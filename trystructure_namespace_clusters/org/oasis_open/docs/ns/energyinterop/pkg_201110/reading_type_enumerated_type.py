from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


class ReadingTypeEnumeratedType(Enum):
    """
    :cvar DIRECT_READ: Reading is read from a device that increases
        monotonically, and usage must be computed from pairs of start
        and stop readings.
    :cvar NET: Meter or [resource] prepares its own calculation of total
        use over time.
    :cvar ALLOCATED: Meter covers several [resources] and usage is
        inferred through some sort of pro data computation.
    :cvar ESTIMATED: Used when a reading is absent in a series in which
        most readings are present.
    :cvar SUMMED: Several meters together provide the reading for this
        [resource]. This is specifically a different than aggregated,
        which refers to multiple [resources] in the same payload. See
        also Hybrid.
    :cvar DERIVED: Usage is inferred through knowledge of run-time,
        normal operation, etc.
    :cvar MEAN: Reading is the mean value over the period indicated in
        Granularity
    :cvar PEAK: Reading is Peak (highest) value over the period
        indicated in granularity. For some measurements, it may make
        more sense as the lowest value. May not be consistent with
        aggregate readings. Only valid for flow-rate Item Bases, i.e.,
        Power not Energy.
    :cvar HYBRID: If aggregated, refers to different reading types in
        the aggregate number.
    :cvar CONTRACT: Indicates reading is pro forma, i.e., is reported at
        agreed upon rates
    :cvar PROJECTED: Indicates reading is in the future, and has not yet
        been measured.
    :cvar X_RMS: Root Mean Square
    :cvar X_NOT_APPLICABLE: Not Applicable
    """
    DIRECT_READ = "Direct Read"
    NET = "Net"
    ALLOCATED = "Allocated"
    ESTIMATED = "Estimated"
    SUMMED = "Summed"
    DERIVED = "Derived"
    MEAN = "Mean"
    PEAK = "Peak"
    HYBRID = "Hybrid"
    CONTRACT = "Contract"
    PROJECTED = "Projected"
    X_RMS = "x-RMS"
    X_NOT_APPLICABLE = "x-notApplicable"
