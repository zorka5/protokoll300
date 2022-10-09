import unittest
from protokoll300.frame import RequestFrame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)


class TestRequestFrameCurrentParams(unittest.TestCase):
    def test_request_frame_slope_M2_1_7_checksum(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x11"],
        )
        self.assertEqual(frame.checksum, b"\x24")

    def test_request_frame_slope_m2_1_7_one_byte(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x11"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x37\xd3\x01\x11\x24")

    def test_request_frame_slope_m2_1_1_one_byte(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M2_HEATING_CURVE_SLOPE.value,
            data=[b"\x0b"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x37\xd3\x01\x0b\x1e")

    def test_request_frame_slope_m3_1_7_one_byte(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M3_HEATING_CURVE_SLOPE.value,
            data=[b"\x11"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x47\xd3\x01\x11\x34")

    def test_request_frame_slope_m3_1_1_one_byte(self):
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_WRITE.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.M3_HEATING_CURVE_SLOPE.value,
            data=[b"\x0b"],
        )
        self.assertEqual(frame.sequence, b"\x41\x06\x00\x02\x47\xd3\x01\x0b\x2e")
