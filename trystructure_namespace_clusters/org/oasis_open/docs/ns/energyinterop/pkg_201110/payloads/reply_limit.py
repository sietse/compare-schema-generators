from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"


@dataclass
class ReplyLimit:
    class Meta:
        name = "replyLimit"
        namespace = "http://docs.oasis-open.org/ns/energyinterop/201110/payloads"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
