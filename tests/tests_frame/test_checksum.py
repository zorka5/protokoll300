import unittest

from protokoll300.frame import Frame, ResponseFrame, RequestFrame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class TestChecksum(unittest.TestCase):
    def test_frame_checksum_current_temp_resp(self):
        frame = Frame("41 05 00 01 08 0C 10 2A")
        self.assertEqual(frame.checksum, b"\x2A")

    def test_frame_checksum_resp_frame_11(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_REQUIRED_ROOM_TEMP_NORMAL_OPERATION,
            data=[b"\x0B", b"\x00"],
        )
        self.assertEqual(frame.checksum, b"\x4E")

    def test_frame_checksum_resp_frame_13(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_REQUIRED_ROOM_TEMP_NORMAL_OPERATION,
            data=[b"\x0D", b"\x00"],
        )
        self.assertEqual(frame.checksum, b"\x50")
