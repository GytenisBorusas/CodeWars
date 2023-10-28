""" This module contains classes for the creation of a mock database. 

    !!! Please do not edit any code in this file, this is intended to act as the database. !!!
"""

import time
from copy import deepcopy
from typing import Optional
from dataclasses import dataclass

class DisconnectedException(Exception):
    pass

@dataclass
class Packet:
    id: int
    name: str

@dataclass
class PacketTelemetryItem:
    id: int
    packet_id: int
    telemetry_item_id: int
    item_number: int

@dataclass
class TelemetryItem:
    id: int
    parent_id: Optional[int]
    name: str
    datatype: str
    item_number: Optional[int]
    enumeration_id: Optional[int]

@dataclass
class TelemetryEnumeration:
    id: int
    name: str

@dataclass
class TelemetryEnumerationValue:
    id: int
    name: str
    value: int
    enumeration_id: int

_packets = [
    Packet(1, "TLM_VEHICLE_FRONT"),
    Packet(2, "TLM_VEHICLE_BACK"),
    Packet(3, "TLM_VEHICLE_WINGS"),
    Packet(4, "TLM_CARGO_MODULE"),
]

_telemetry_items = [
    TelemetryItem(1, None,   "NOSE_PRESSURE_AND_TEMP",   "struct",   None,  None),
    TelemetryItem(2, 1,      "NOSE_PRESSURE_1",          "uint_32",  0,     None),
    TelemetryItem(3, 1,      "NOSE_TEMP_1",              "uint_32",  1,     None),
    TelemetryItem(4, 1,      "NOSE_PRESSURE_2",          "uint_32",  2,     None),
    TelemetryItem(5, 1,      "NOSE_TEMP_2",              "uint_32",  3,     None),
    
    TelemetryItem(6, None,   "FRONT_POWER",              "struct",   None,  None),
    TelemetryItem(7, 6,      "FRONT_POWERED_ON",         "enum",     0,     1),
    TelemetryItem(8, 6,      "FRONT_VOLTAGE",            "int_16",   1,     None),

    TelemetryItem(9,  None,  "MAIN_ECLSS",               "struct",   None,  None),
    TelemetryItem(10, 9,     "O2_CONCENTRATION",         "int_16",   0,     None),
    TelemetryItem(11, 9,     "CO2_CONCENTRATION",        "int_16",   1,     None),
    TelemetryItem(12, 9,     "UNIT_POWER",               "struct",   2,     None),
    TelemetryItem(13, 12,    "POWERED_ON",               "enum",     0,     1),
    TelemetryItem(14, 12,    "VOLTAGE",                  "int_32",   1,     None),
    TelemetryItem(15, 9,     "CURRENT_STATE",            "enum",     3,     2),

    TelemetryItem(16, None,  "BACKUP_ECLSS",             "struct",   None,  None),
    TelemetryItem(17, 16,    "O2_CONCENTRATION",         "int_16",   0,     None),
    TelemetryItem(18, 16,    "CO2_CONCENTRATION",        "int_16",   1,     None),
    TelemetryItem(19, 16,    "UNIT_POWER",               "struct",   2,     None),
    TelemetryItem(20, 19,    "POWERED_ON",               "enum",     0,     1),
    TelemetryItem(21, 19,    "VOLTAGE",                  "int_32",   1,     None),
    TelemetryItem(22, 16,    "CURRENT_STATE",            "enum",     3,     2),

    TelemetryItem(23, None,  "CONTROL_SURFACES",         "struct",   None,  None),
    TelemetryItem(24, 23,    "SURFACE_1_POWER",          "int_16",   0,     None),
    TelemetryItem(25, 23,    "SURFACE_1_ROTATION",       "uint_32",  1,     None),
    TelemetryItem(26, 23,    "SURFACE_2_POWER",          "int_16",   2,     None),
    TelemetryItem(27, 23,    "SURFACE_2_ROTATION",       "uint_32",  3,     None),
    
    TelemetryItem(28, None,  "DEPLOYMENT",               "struct",   None,  None),
    TelemetryItem(29, 28,    "LEFT_WING_DEPLOYED",       "bool",     0,     None),
    TelemetryItem(30, 28,    "LEFT_WING_ROTATION",       "uint_32",  1,     None),
    TelemetryItem(31, 28,    "RIGHT_WING_DEPLOYED",      "bool",     2,     None),
    TelemetryItem(32, 28,    "RIGHT_WING_ROTATION",      "uint_32",  3,     None),

    TelemetryItem(33, None,  "MAIN_CARGO_ECLSS",         "struct",   None,  None),
    TelemetryItem(34, 33,    "O2_CONCENTRATION",        "int_16",    0,     None),
    TelemetryItem(35, 33,    "CO2_CONCENTRATION",       "int_16",    1,     None),
    TelemetryItem(36, 33,    "UNIT_POWER",              "struct",    2,     None),
    TelemetryItem(37, 36,    "POWERED_ON",              "enum",      0,     1),
    TelemetryItem(38, 36,    "VOLTAGE",                 "int_32",    1,     None),
    TelemetryItem(39, 33,    "CURRENT_STATE",           "enum",      3,     2),

    TelemetryItem(40, None,  "BACKUP_CARGO_ECLSS",       "struct",   None,  None),
    TelemetryItem(41, 40,    "O2_CONCENTRATION",         "int_16",   0,     None),
    TelemetryItem(42, 40,    "CO2_CONCENTRATION",        "int_16",   1,     None),
    TelemetryItem(43, 40,    "UNIT_POWER",               "struct",   2,     None),
    TelemetryItem(44, 43,    "POWERED_ON",               "enum",     0,     1),
    TelemetryItem(45, 43,    "VOLTAGE",                  "int_32",   1,     None),
    TelemetryItem(46, 40,    "CURRENT_STATE",            "enum",     3,     2),

    TelemetryItem(47, None,  "CARGO_SOLAR_PANELS",       "struct",   None,  None),
    TelemetryItem(48, 47,    "PANEL_1_ROTATION",         "uint_16",  0,     None),
    TelemetryItem(49, 47,    "PANEL_2_ROTATION",         "uint_16",  1,     None),
    TelemetryItem(50, 47,    "PANEL_3_ROTATION",         "uint_16",  2,     None),
    TelemetryItem(51, 47,    "PANEL_4_ROTATION",         "uint_16",  3,     None),
    TelemetryItem(52, 47,    "PANEL_1_DEPLOYED",         "bool",     4,     None),
    TelemetryItem(53, 47,    "PANEL_2_DEPLOYED",         "bool",     5,     None),
    TelemetryItem(54, 47,    "PANEL_3_DEPLOYED",         "bool",     6,     None),
    TelemetryItem(55, 47,    "PANEL_4_DEPLOYED",         "bool",     7,     None),

    TelemetryItem(56, None,  "CARGO_FUEL_TANKS",           "struct", None,  None),
    TelemetryItem(57, 56,    "FUEL_TANK_1_PRESSURE",       "int_16", 0,     None),
    TelemetryItem(58, 56,    "FUEL_TANK_2_PRESSURE",       "int_16", 1,     None),
    TelemetryItem(59, 56,    "FUEL_TANK_1_FUEL_REMAINING", "int_32", 2,     None),
    TelemetryItem(60, 56,    "FUEL_TANK_2_FUEL_REMAINING", "int_32", 3,     None),

    TelemetryItem(61, None,  "CARGO_MODULE_ATTACHED",      "enum",   None,  3),
]

_packet_telemetry_items = [
    PacketTelemetryItem(1, 1, 1, 0),
    PacketTelemetryItem(2, 1, 6, 1),
    PacketTelemetryItem(3, 2, 9, 0),
    PacketTelemetryItem(4, 2, 16, 1),
    PacketTelemetryItem(5, 3, 23, 0),
    PacketTelemetryItem(6, 3, 28, 1),
    PacketTelemetryItem(7, 4, 33, 0),
    PacketTelemetryItem(8, 4, 40, 1),
    PacketTelemetryItem(9, 4, 47, 2),
    PacketTelemetryItem(10, 4, 56, 3),
    PacketTelemetryItem(11, 4, 61, 4),
]

_telemetry_enums = [
    TelemetryEnumeration(1, "POWERED_ON"),
    TelemetryEnumeration(2, "ECLSS_STATE"),
    TelemetryEnumeration(3, "BOOLEAN"),
]

_telemetry_enum_values = [
    TelemetryEnumerationValue(1, "NO",       0, 1),
    TelemetryEnumerationValue(2, "YES",      1, 1),
    TelemetryEnumerationValue(3, "DISABLED", 0, 2),
    TelemetryEnumerationValue(4, "NOMINAL",  1, 2),
    TelemetryEnumerationValue(5, "FAULTED",  2, 2),
    TelemetryEnumerationValue(6, "UNKNOWN",  3, 2),
    TelemetryEnumerationValue(7, "FALSE",    0, 3),
    TelemetryEnumerationValue(8, "TRUE",     1, 3),
]

class DatabaseHelper:
    """ This is a mock database connector. To use, create an instance, and use the connect function to establish a connection. 
        Then use the other functions to query data. """
    connected: bool

    def __init__(self):
        self.connected = False

    def connect_to_database(self, hostname: str, schema: str, username: str, password: str) -> None:
        """ Connect to the database """
        self.connected = True
        return

    def get_packets(self) -> list[Packet]:
        if not self.connected:
            raise DisconnectedException()
        time.sleep(0.2) # simulate network latency
        return deepcopy(_packets)

    def get_telemetry_items(self) -> list[TelemetryItem]:
        if not self.connected:
            raise DisconnectedException()
        time.sleep(0.2) # simulate network latency
        return deepcopy(_telemetry_items)
    
    def get_packet_telemetry_items(self) -> list[PacketTelemetryItem]:
        if not self.connected:
            raise DisconnectedException()
        time.sleep(0.2) # simulate network latency
        return deepcopy(_packet_telemetry_items)
    
    def get_telemetry_enums(self) -> list[TelemetryEnumeration]:
        if not self.connected:
            raise DisconnectedException()
        time.sleep(0.2) # simulate network latency
        return deepcopy(_telemetry_enums)
    
    def get_telemetry_enum_values(self) -> list[TelemetryEnumerationValue]:
        if not self.connected:
            raise DisconnectedException()
        time.sleep(1) # simulate network latency
        return deepcopy(_telemetry_enum_values)
