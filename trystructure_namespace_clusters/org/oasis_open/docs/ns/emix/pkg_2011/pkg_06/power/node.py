from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass
class Node:
    class Meta:
        name = "node"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
