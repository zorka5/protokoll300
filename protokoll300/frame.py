class Frame:
    """
    Class representing standard protokoll300 frame.
    """

    _frame_sequence: bytearray
    _start_byte: bytes
    _frame_length: bytes
    _unit_identifier: bytes
    _function_code: bytes
    _address: bytearray
    _control_sum: bytes

    def __init__(self, frame_string: str) -> None:
        self._frame_sequence = bytearray.fromhex(frame_string)
        self._start_byte = self._frame_sequence[0].to_bytes(1, "little")
        self._frame_length = self._frame_sequence[1].to_bytes(1, "little")
        self._unit_identifier = self._frame_sequence[2].to_bytes(1, "little")
        self._function_code = self._frame_sequence[3].to_bytes(1, "little")
        self._address = bytearray(
            [
                self._frame_sequence[4],
                self._frame_sequence[5],
            ]
        )
        self._control_sum = int.to_bytes(self.calculate_checksum(), 1, "little")
        self._frame_sequence += self._control_sum

    def calculate_checksum(self) -> int:
        """
        Method used to calculate checksum by adding bytes from second to last,
        determined by frame length property.
        """
        frame_length = int.from_bytes(self._frame_length, "little")
        dec = list(self._frame_sequence[1 : frame_length + 2])
        return sum(dec) % 256

    @property
    def sequence(self) -> bytearray:
        "Property of frame byte sequence"
        return self._frame_sequence

    @property
    def checksum(self) -> int:
        "Property of frame checksum"
        return self.calculate_checksum()


class RequestFrame(Frame):
    "Class representing request frame"
    _expected_data_length: int

    def __init__(
        self,
        start_byte: bytes,
        unit_identifier: bytes,
        function_code: bytes,
        procedure_adress_and_length: tuple[bytes, bytes, int],
    ) -> None:
        self._expected_data_length = procedure_adress_and_length[2]

        data_length_bytes = procedure_adress_and_length[2].to_bytes(1, "little")

        frame_list = [
            start_byte,
            unit_identifier,
            function_code,
            procedure_adress_and_length[0],
            procedure_adress_and_length[1],
            data_length_bytes,
        ]

        length_byte = (len(frame_list) - 1).to_bytes(1, "little")
        frame_list.insert(1, length_byte)
        frame_bytes = b"".join(frame_list)
        super().__init__(frame_string=frame_bytes.hex())


# pylint: disable=pylint(too-many-arguments)


class ResponseFrame(Frame):
    "class representing response frame"
    _data_length: int
    _data: list[bytes]

    def __init__(
        self,
        start_byte: bytes,
        unit_identifier: bytes,
        function_code: bytes,
        procedure_adress_and_length: tuple[bytes, bytes, int],
        data: list[bytes],
    ) -> None:
        self._data_length = procedure_adress_and_length[2]
        self._data = data
        frame_list = [
            start_byte,
            unit_identifier,
            function_code,
            procedure_adress_and_length[0],
            procedure_adress_and_length[1],
            procedure_adress_and_length[2].to_bytes(1, "little"),
        ]
        frame_list += data
        frame_list.insert(1, (len(frame_list) - 1).to_bytes(1, "little"))
        frame_bytes = b"".join(frame_list)
        super().__init__(frame_string=frame_bytes.hex())
