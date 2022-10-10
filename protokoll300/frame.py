from dataclasses import dataclass
from .utils import sum_bytes_mod_256
from .codes import START_BYTE, UnitIdentifier, FunctionCodes, ProcedureAdresses, ExpectedLength


@dataclass
class Frame:
    """
    Class representing standard protokoll300 frame.
    """

    frame_sequence: bytes
    start_byte: bytes
    frame_length: bytes
    unit_identifier: bytes
    function_code: bytes
    address: bytes
    data_length: bytes
    data: bytes
    control_sum: bytes

    def __init__(self, frame_bytes: bytes) -> None:
        self.frame_sequence = frame_bytes
        self.start_byte = frame_bytes[0].to_bytes(1, "little")
        self.frame_length = frame_bytes[1].to_bytes(1, "little")
        self.unit_identifier = frame_bytes[2].to_bytes(1, "little")
        self.function_code = frame_bytes[3].to_bytes(1, "little")
        self.address = frame_bytes[4:6]
        self.data_length = frame_bytes[6].to_bytes(1, "little")
        self.data = frame_bytes[7:][:-1]
        self.control_sum = frame_bytes[-1].to_bytes(1, "little")

    
    def is_ok(self) -> bool:
        """
        Method used to calculate checksum by adding bytes from second to last,
        determined by frame length property.
        """
        frame_length = int.from_bytes(self.frame_length, "little")
        dec = list(self.frame_sequence[1 : frame_length + 2])
        return sum(dec) % 256 == int.from_bytes(self.control_sum, "little")

@staticmethod
def parse_data(
    start_byte: bytes,
    unit_identifier: UnitIdentifier,
    function_code: FunctionCodes,
    procedure_address: ProcedureAdresses,
    expected_length: ExpectedLength,
    data: bytes,
) -> Frame:
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
    return Frame(b"".join(
        [
            start_byte,
            bs,
            control_sum,
        ]
    ))