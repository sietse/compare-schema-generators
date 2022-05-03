from dataclasses import dataclass
from trystructure_clusters.ei_target_type import EiTargetType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportDataSource(EiTargetType):
    """Sources for data in this report.

    Examples include meters or submeters. For example, if a meter is
    capable of providing two different types of measurements, then each
    measurement stream would be separately identified.
    """
    class Meta:
        name = "reportDataSource"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
