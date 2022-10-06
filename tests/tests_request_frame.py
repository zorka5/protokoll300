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
            function_code=FunctionCodes.VIRTUAL_READ.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
        )
        self.assertEqual(frame.checksum, 42)

    def test_request_frame_current_params(self):
        "Method to check frame requesting current params"
        frame = RequestFrame(
            start_byte=b"\x41",
            unit_identifier=UnitIdentifier.REQUEST.value,
            function_code=FunctionCodes.VIRTUAL_READ.value,
            procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
        )
        self.assertEqual(frame.sequence, b"\x41\x05\x00\x01\x08\x0C\x10\x2A")


if __name__ == "__main__":
    unittest.main()
