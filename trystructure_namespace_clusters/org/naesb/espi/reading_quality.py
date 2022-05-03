from dataclasses import dataclass, field
from typing import Optional, Union
from trystructure_namespace_clusters.org.naesb.espi.object_mod import Object
from trystructure_namespace_clusters.org.naesb.espi.quality_of_reading_value import QualityOfReadingValue

__NAMESPACE__ = "http://naesb.org/espi"


@dataclass
class ReadingQuality(Object):
    """Quality of a specific reading value or interval reading value.

    Note that more than one Quality may be applicable to a given
    Reading. Typically not used unless problems or unusual conditions
    occur (i.e., quality for each Reading is assumed to be 'Good'
    (valid) unless stated otherwise in associated ReadingQuality).

    :ivar quality: Quality, to be specified if different than
        ReadingType.defaultQuality. The specific format is specified per
        the standard is defined in QualityOfReading.
    """
    class Meta:
        namespace = "http://naesb.org/espi"

    quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
