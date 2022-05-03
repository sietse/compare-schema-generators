from enum import Enum

__NAMESPACE__ = "http://openadr.org/oadr-2.0b/2012/07"


class OadrDataQualityType(Enum):
    NO_QUALITY_NO_VALUE = "No Quality - No Value"
    NO_NEW_VALUE_PREVIOUS_VALUE_USED = "No New Value - Previous Value Used"
    QUALITY_BAD_NON_SPECIFIC = "Quality Bad - Non Specific"
    QUALITY_BAD_CONFIGURATION_ERROR = "Quality Bad - Configuration Error"
    QUALITY_BAD_NOT_CONNECTED = "Quality Bad - Not Connected"
    QUALITY_BAD_DEVICE_FAILURE = "Quality Bad - Device Failure"
    QUALITY_BAD_SENSOR_FAILURE = "Quality Bad - Sensor Failure"
    QUALITY_BAD_LAST_KNOWN_VALUE = "Quality Bad - Last Known Value"
    QUALITY_BAD_COMM_FAILURE = "Quality Bad - Comm Failure"
    QUALITY_BAD_OUT_OF_SERVICE = "Quality Bad - Out of Service"
    QUALITY_UNCERTAIN_NON_SPECIFIC = "Quality Uncertain - Non Specific"
    QUALITY_UNCERTAIN_LAST_USABLE_VALUE = "Quality Uncertain - Last Usable Value"
    QUALITY_UNCERTAIN_SENSOR_NOT_ACCURATE = "Quality Uncertain - Sensor Not Accurate"
    QUALITY_UNCERTAIN_EU_UNITS_EXCEEDED = "Quality Uncertain - EU Units Exceeded"
    QUALITY_UNCERTAIN_SUB_NORMAL = "Quality Uncertain - Sub Normal"
    QUALITY_GOOD_NON_SPECIFIC = "Quality Good - Non Specific"
    QUALITY_GOOD_LOCAL_OVERRIDE = "Quality Good - Local Override"
    QUALITY_LIMIT_FIELD_NOT = "Quality Limit - Field/Not"
    QUALITY_LIMIT_FIELD_LOW = "Quality Limit - Field/Low"
    QUALITY_LIMIT_FIELD_HIGH = "Quality Limit - Field/High"
    QUALITY_LIMIT_FIELD_CONSTANT = "Quality Limit - Field/Constant"
