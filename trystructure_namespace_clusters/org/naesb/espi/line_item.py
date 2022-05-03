from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class LineItem:
    """
    [extension] Line item of detail for additional cost.
    """
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    rounding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        }
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )
