import unittest
from protokoll300.frame import RequestFrame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)


class TestRequestFrameCurrentParams(unittest.TestCase):
    "Class to test Request frames"

    def test_request_frame_slope_M2_checksum(self):
        "Method to check checksum calculation"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.RESPONSE.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x0B"],
        )
        self.assertEqual(frame.checksum, b"\x2A")

    def test_request_frame_slope_1_1_one_byte(self):
        "Method to check frame requesting setting slope"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x0B"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x37\xd3\x01\xB0\x2A")

    def test_request_frame_slope_1_1_two_bytes(self):
        "Method to check frame requesting setting slope"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_READ.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x0B"],
        )
        self.assertEqual(frame.sequence, b"\x41\x07\x00\x02\x37\xd3\x02\xB0\x00\x2A")
