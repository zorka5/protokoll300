from enum import Enum

START_BYTE = b"\x41"


class UnitIdentifier(bytes, Enum):
    REQUEST = b"\x00"
    RESPONSE = b"\x01"
    UNACKD = b"\x02"
    ERROR = b"\x03"


class FunctionCodes(bytes, Enum):
    VIRTUAL_READ = b"\x01"
    VIRTUAL_WRITE = b"\x02"
    REMOTE_PROCEDURE_CALL = b"\x07"


class ProcedureAdressesAndExpectedLength(tuple[bytes, bytes, int], Enum):
    CURRENT_PARAMS = (b"\x08", b"\x0C", 16)
    OUTDOOR_TEMP = (b"\x55", b"\x25", 4)
    BOILER_WATER_TEMP = (b"\x29", b"\x00", 7)
    M2_REQUIRED_ROOM_TEMP_NORMAL_OPERATION = (b"\x33", b"\x06", 1)
    M3_REQUIRED_ROOM_TEMP_NORMAL_OPERATION = (b"\x43", b"\x06", 1)
    M2_HEATING_CURVE_SLOPE = (b"\x37", b"\xD3", 1)
    M3_HEATING_CURVE_SLOPE = (b"\x47", b"\xD3", 1)
    M2_HEATING_CURVE_LEVEL = (b"\x37", b"\xD4", 1)
    M3_HEATING_CURVE_LEVEL = (b"\x47", b"\xD4", 1)


class ExceptionCode(bytes, Enum):
    ILLEGAL_FUNCTION = b"\x01"
    ILLEGAL_DATA_ADDRESS = b"\x02"
    ILLEGAL_DATA_VALUE = b"\x03"
    SERVER_DEVICE_FAILURE = b"\x04"
    ACKNOWLEDGE = b"\x05"
    SERVER_DEVICE_BUSY = b"\x06"
    NEGATIVE_ACKNOWLEDGE = b"\x07"
    MEMORY_PARITY_ERROR = b"\x08"
    GATEWAY_PATH_ANAVAILABLE = b"\xA0"
    GATEWAY_TARGET_DEVICE_FAILED_TO_RESPOND = b"\xB0"
