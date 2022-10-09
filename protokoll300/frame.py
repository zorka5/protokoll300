from dataclasses import dataclass


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
