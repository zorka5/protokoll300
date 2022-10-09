import unittest
from protokoll300.frame import ResposeFrame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)


class TestResponseFrameSlope(unittest.TestCase):
    "Class to test Request frames"

    def test_resp_frame_slope_checksum(self):
        "Method to check checksum calculation"
        frame = ResposeFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_READ.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
        )
        self.assertEqual(frame.checksum, 42)

    def test_resp_frame_slope(self):
        "Method to check frame resping current params"
        frame = ResposeFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_READ.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
        )
        self.assertEqual(frame.sequence, b"\x41\x05\x00\x01\x08\x0C\x10\x2A")
