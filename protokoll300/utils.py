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
    data: bytes,
) -> bytes:
    frame_length = (
        len(unit_identifier.value)
        + len(function_code.value)
        + len(procedure_address.value)
        + len(expected_length.value)
        + len(data)
    ).to_bytes(1, "little")

    bs = b"".join(
        [
            frame_length,
            unit_identifier.value,
            function_code.value,
            procedure_address.value,
            expected_length.value,
            data,
        ]
    )

    control_sum = sum_bytes_mod_256(bs)
    return b"".join(
        [
            start_byte,
            bs,
            control_sum,
        ]
    )
