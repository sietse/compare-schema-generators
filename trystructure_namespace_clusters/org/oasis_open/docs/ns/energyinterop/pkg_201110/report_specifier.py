from dataclasses import dataclass
from trystructure_namespace_clusters.org.oasis_open.docs.ns.energyinterop.pkg_201110.report_specifier_type import ReportSpecifierType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class ReportSpecifier(ReportSpecifierType):
    """
    Specify data points desired in a particular report instance.
    """
    class Meta:
        name = "reportSpecifier"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
