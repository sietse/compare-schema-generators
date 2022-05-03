from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from tryoptions_unsafe_hashes.oadr_emix_20b import ItemBaseType
from tryoptions_unsafe_hashes.oadr_gml_20b import FeatureCollection
from tryoptions_unsafe_hashes.oadr_siscale_20b import SiScaleCodeType

__NAMESPACE__ = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class AggregatedPnodeType:
    """
    An aggregated pricing node is a specialized type of pricing node used to
    model items such as System Zone, Default Price Zone, Custom Price Zone,
    Control Area, Aggregated Generation, Aggregated Participating Load,
    Aggregated Non-Participating Load, Trading Hub, DCA Zone.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class EndDeviceAssetType:
    """
    The EndDeviceAssets are the physical device or devices which could be
    meters or other types of devices that may be of interest.
    """
    mrid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class MeterAssetType:
    """
    The MeterAsset is the physical device or devices that performs the role of
    the meter.
    """
    mrid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class PnodeType:
    """A pricing node is directly associated with a connectivity node.

    It is a pricing location for which market participants submit their
    bids, offers, buy/sell CRRs, and settle.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class PowerAttributesType:
    hertz: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    ac: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


class PowerRealTypeItemUnits(Enum):
    W = "W"
    J_S = "J/s"


@dataclass(unsafe_hash=True, frozen=True)
class ServiceDeliveryPointType:
    """Logical point on the network where the ownership of the service changes
    hands.

    It is one of potentially many service points within a
    ServiceLocation, delivering service in accordance with a
    CustomerAgreement. Used at the place where a meter may be installed.
    """
    node: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class TransportInterfaceType:
    """
    The Transport Interface delineates the edges at either end of a transport
    segment.
    """
    point_of_receipt: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfReceipt",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    point_of_delivery: Optional[str] = field(
        default=None,
        metadata={
            "name": "pointOfDelivery",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class Mrid:
    class Meta:
        name = "mrid"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
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


@dataclass(unsafe_hash=True, frozen=True)
class EnergyItemType(ItemBaseType):
    """
    Base for the measurement of Energy.
    """
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class ServiceLocationType:
    """A customer ServiceLocation has one or more ServiceDeliveryPoint(s),
    which in turn relate to Meters.

    The location may be a point or a polygon, depending on the specific
    circumstances. For distribution, the ServiceLocation is typically
    the location of the utility customer's premise.
    """
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class VoltageType(ItemBaseType):
    """
    Voltage.
    """
    item_description: str = field(
        init=False,
        default="Voltage",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="V",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class AggregatedPnode(AggregatedPnodeType):
    class Meta:
        name = "aggregatedPnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class EndDeviceAsset(EndDeviceAssetType):
    class Meta:
        name = "endDeviceAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class MeterAsset(MeterAssetType):
    class Meta:
        name = "meterAsset"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class Pnode(PnodeType):
    class Meta:
        name = "pnode"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerAttributes(PowerAttributesType):
    class Meta:
        name = "powerAttributes"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class ServiceDeliveryPoint(ServiceDeliveryPointType):
    class Meta:
        name = "serviceDeliveryPoint"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class TransportInterface(TransportInterfaceType):
    class Meta:
        name = "transportInterface"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class EnergyApparentType(EnergyItemType):
    """
    Apparent Energy, measured in volt-ampere hours (VAh)
    """
    item_description: str = field(
        init=False,
        default="ApparentEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class EnergyReactiveType(EnergyItemType):
    """
    Reactive Energy, volt-amperes reactive hours (VARh)
    """
    item_description: str = field(
        init=False,
        default="ReactiveEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VARh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class EnergyRealType(EnergyItemType):
    """
    Real Energy, Watt Hours (Wh)
    """
    item_description: str = field(
        init=False,
        default="RealEnergy",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="Wh",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class PowerItemType(ItemBaseType):
    """
    Base for the measurement of Power.
    """
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    si_scale_code: Optional[SiScaleCodeType] = field(
        default=None,
        metadata={
            "name": "siScaleCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/siscale",
            "required": True,
        }
    )
    power_attributes: Optional[PowerAttributes] = field(
        default=None,
        metadata={
            "name": "powerAttributes",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class EnergyItem(EnergyItemType):
    class Meta:
        name = "energyItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class ServiceLocation(ServiceLocationType):
    class Meta:
        name = "serviceLocation"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class Voltage(VoltageType):
    class Meta:
        name = "voltage"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerApparentType(PowerItemType):
    """
    Apparent Power measured in volt-amperes (VA)
    """
    item_description: str = field(
        init=False,
        default="ApparentPower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VA",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class PowerReactiveType(PowerItemType):
    """
    Reactive power, measured in volt-amperes reactive (VAR)
    """
    item_description: str = field(
        init=False,
        default="ReactivePower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )
    item_units: str = field(
        init=False,
        default="VAR",
        metadata={
            "name": "itemUnits",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class PowerRealType(PowerItemType):
    """
    Real power measured in Watts (W) or Joules/second (J/s)
    """
    item_description: str = field(
        init=False,
        default="RealPower",
        metadata={
            "name": "itemDescription",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, frozen=True)
class EnergyApparent(EnergyApparentType):
    class Meta:
        name = "energyApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class EnergyReactive(EnergyReactiveType):
    class Meta:
        name = "energyReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class EnergyReal(EnergyRealType):
    class Meta:
        name = "energyReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerItem(PowerItemType):
    class Meta:
        name = "powerItem"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerApparent(PowerApparentType):
    class Meta:
        name = "powerApparent"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerReactive(PowerReactiveType):
    class Meta:
        name = "powerReactive"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"


@dataclass(unsafe_hash=True, frozen=True)
class PowerReal(PowerRealType):
    class Meta:
        name = "powerReal"
        namespace = "http://docs.oasis-open.org/ns/emix/2011/06/power"
