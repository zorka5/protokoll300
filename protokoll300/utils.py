from typing import Optional
from protokoll300.codes import (
    START_BYTE,
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdresses,
    ExpectedLength,
)


def isolate_frame(frame: bytes, start_byte: bytes) -> Optional[bytes]:
    """
    Function isolating frame from given bytes.
    Function searches for starting byte and returns frame starting with it.
    Params:
        -frame - given frame to isolate
        -start_byte - given start byte
    Return:
        isolated frame or None if not found
    """
    try:
        frame = frame[frame.index(start_byte) :]
        return frame
    except ValueError:
        print("no start byte in frame")
    return None


def sum_bytes_mod_256(bytes_list: bytes) -> bytes:
    sum = 0
    for byte in bytes_list:
        sum += byte
    return (sum % 256).to_bytes(1, "little")


def parse_data(
    start_byte: bytes,
    unit_identifier: UnitIdentifier,
    function_code: FunctionCodes,
    procedure_address: ProcedureAdresses,
    expected_length: ExpectedLength,
) -> bytes:
    bytes_list: list[bytes] = [
        start_byte,
        unit_identifier.value,
        function_code.value,
        procedure_address.value,
        expected_length.value,
    ]
    bytes_list.insert(1, (len(bytes_list)).to_bytes(1, "little"))
    checksum: bytes = sum_bytes_mod_256(b"".join(bytes_list[1:]))
    bytes_list.append(checksum)
    return b"".join(bytes_list)
