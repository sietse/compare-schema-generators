from enum import Enum

__NAMESPACE__ = "http://naesb.org/espi"


class StatusCodeValue(Enum):
    VALUE_200 = 200
    VALUE_201 = 201
    VALUE_204 = 204
    VALUE_301 = 301
    VALUE_302 = 302
    VALUE_304 = 304
    VALUE_400 = 400
    VALUE_401 = 401
    VALUE_403 = 403
    VALUE_404 = 404
    VALUE_405 = 405
    VALUE_410 = 410
    VALUE_500 = 500
