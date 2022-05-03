from enum import Enum

__NAMESPACE__ = "http://docs.oasis-open.org/ns/energyinterop/201110"


class SignalNameEnumeratedType(Enum):
    """
    :cvar SIMPLE: Simple levels (OpenADR 2.0a compliant)
    :cvar SIMPLE_1: depreciated - for backwards compatibility with A
        profile
    :cvar ELECTRICITY_PRICE: This is the cost of electricity
    :cvar ENERGY_PRICE: This is the cost of energy
    :cvar DEMAND_CHARGE: This is the demand charge
    :cvar BID_PRICE: This is the price that was bid by the resource
    :cvar BID_LOAD: This is the amount of load that was bid by a
        resource into a program
    :cvar BID_ENERGY: This is the amount of energy from a resource that
        was bid into a program
    :cvar CHARGE_STATE: State of energy storage resource
    :cvar LOAD_DISPATCH: This is used to dispatch load
    :cvar LOAD_CONTROL: Set load output to relative values
    """
    SIMPLE = "SIMPLE"
    SIMPLE_1 = "simple"
    ELECTRICITY_PRICE = "ELECTRICITY_PRICE"
    ENERGY_PRICE = "ENERGY_PRICE"
    DEMAND_CHARGE = "DEMAND_CHARGE"
    BID_PRICE = "BID_PRICE"
    BID_LOAD = "BID_LOAD"
    BID_ENERGY = "BID_ENERGY"
    CHARGE_STATE = "CHARGE_STATE"
    LOAD_DISPATCH = "LOAD_DISPATCH"
    LOAD_CONTROL = "LOAD_CONTROL"
