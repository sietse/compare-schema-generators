from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class CharTwoFieldParamsType:
    m: Optional[int] = field(
        default=None,
        metadata={
            "name": "M",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class CurveType:
    a: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    b: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "B",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class DerencodedKeyValueType:
    class Meta:
        name = "DEREncodedKeyValueType"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class EcvalidationDataType:
    class Meta:
        name = "ECValidationDataType"

    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    hash_algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "hashAlgorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KeyInfoReferenceType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class NamedCurveType:
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrimeFieldParamsType:
    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class X509DigestType:
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DerencodedKeyValue(DerencodedKeyValueType):
    class Meta:
        name = "DEREncodedKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class GnB(CharTwoFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class KeyInfoReference(KeyInfoReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "PnBFieldParamsType"

    k1: Optional[int] = field(
        default=None,
        metadata={
            "name": "K1",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k2: Optional[int] = field(
        default=None,
        metadata={
            "name": "K2",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    k3: Optional[int] = field(
        default=None,
        metadata={
            "name": "K3",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class Prime(PrimeFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "TnBFieldParamsType"

    k: Optional[int] = field(
        default=None,
        metadata={
            "name": "K",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )


@dataclass
class X509Digest(X509DigestType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class PnB(PnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class TnB(TnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass
class FieldIdtype:
    class Meta:
        name = "FieldIDType"

    prime: Optional[Prime] = field(
        default=None,
        metadata={
            "name": "Prime",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    tn_b: Optional[TnB] = field(
        default=None,
        metadata={
            "name": "TnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    pn_b: Optional[PnB] = field(
        default=None,
        metadata={
            "name": "PnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    gn_b: Optional[GnB] = field(
        default=None,
        metadata={
            "name": "GnB",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class EcparametersType:
    class Meta:
        name = "ECParametersType"

    field_id: Optional[FieldIdtype] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    curve: Optional[CurveType] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
        }
    )
    base: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    order: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    co_factor: Optional[int] = field(
        default=None,
        metadata={
            "name": "CoFactor",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    validation_data: Optional[EcvalidationDataType] = field(
        default=None,
        metadata={
            "name": "ValidationData",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )


@dataclass
class EckeyValueType:
    class Meta:
        name = "ECKeyValueType"

    ecparameters: Optional[EcparametersType] = field(
        default=None,
        metadata={
            "name": "ECParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    named_curve: Optional[NamedCurveType] = field(
        default=None,
        metadata={
            "name": "NamedCurve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    public_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PublicKey",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class EckeyValue(EckeyValueType):
    class Meta:
        name = "ECKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"
