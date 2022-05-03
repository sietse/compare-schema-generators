from dataclasses import dataclass

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class RegistrationId:
    """Identifier for Registration transaction.

    Not included in response to query registration unless already
    registered
    """
    class Meta:
        name = "registrationID"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110"
