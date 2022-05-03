from dataclasses import dataclass

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class RefId:
    """Reference ID for a particular instance, transmittal, or artifact.

    Note: not the same as the native ID of the object being transmitted or shared.
    """
    class Meta:
        name = "refID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
