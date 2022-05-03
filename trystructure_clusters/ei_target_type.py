from dataclasses import dataclass, field
from typing import List
from trystructure_clusters.aggregated_pnode import AggregatedPnode
from trystructure_clusters.end_device_asset import EndDeviceAsset
from trystructure_clusters.meter_asset import MeterAsset
from trystructure_clusters.pnode import Pnode
from trystructure_clusters.service_area import ServiceArea
from trystructure_clusters.service_delivery_point import ServiceDeliveryPoint
from trystructure_clusters.service_location import ServiceLocation
from trystructure_clusters.transport_interface import TransportInterface

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


@dataclass
class EiTargetType:
    aggregated_pnode: List[AggregatedPnode] = field(
        default_factory=list,
        metadata={
            "name": "aggregatedPnode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    end_device_asset: List[EndDeviceAsset] = field(
        default_factory=list,
        metadata={
            "name": "endDeviceAsset",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    meter_asset: List[MeterAsset] = field(
        default_factory=list,
        metadata={
            "name": "meterAsset",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    pnode: List[Pnode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    service_area: List[ServiceArea] = field(
        default_factory=list,
        metadata={
            "name": "serviceArea",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06",
        }
    )
    service_delivery_point: List[ServiceDeliveryPoint] = field(
        default_factory=list,
        metadata={
            "name": "serviceDeliveryPoint",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    service_location: List[ServiceLocation] = field(
        default_factory=list,
        metadata={
            "name": "serviceLocation",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    transport_interface: List[TransportInterface] = field(
        default_factory=list,
        metadata={
            "name": "transportInterface",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/emix/2011/06/power",
        }
    )
    group_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    group_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    resource_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "resourceID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    ven_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "venID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
    party_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "partyID",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/ns/energyinterop/201110",
        }
    )
