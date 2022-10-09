import unittest
from protokoll300.frame import RequestFrame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)


class TestRequestFrame(unittest.TestCase):
    "Class to test Request frames"

    def test_request_frame_checksum(self):
        "Method to check checksum calculation"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_REQUIRED_ROOM_TEMP_NORMAL_OPERATION,
            data=[b"\x0D", b"\x00"],
        )
        self.assertEqual(frame.sequence, b"\x41\x07\x00\x02\x33\x06\x01\x0D\x00\x50")

    def test_request_frame_checksum_one_byte(self):
        "Method to check checksum calculation"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_REQUIRED_ROOM_TEMP_NORMAL_OPERATION,
            data=[b"\x0D"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x33\x06\x01\x0D\x4F")
