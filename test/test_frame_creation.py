import unittest
from protokoll300.frame import Frame, parse_data
from protokoll300.codes import (
    START_BYTE,
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdresses,
    ExpectedLength,
)


class TestFrameCreation(unittest.TestCase):
    def test_frame_current_params_request(self):
        frame = parse_data(
                START_BYTE,
                UnitIdentifier.REQUEST,
                FunctionCodes.VIRTUAL_READ,
                ProcedureAdresses.CURRENT_PARAMS,
                ExpectedLength.CURRENT_PARAMS,
                data=b"",
            )
        
        self.assertEqual(frame.frame_sequence, b"\x41\x05\x00\x01\x08\x0C\x10\x2A")
        self.assertEqual(frame.start_byte, b"\x41")
        self.assertEqual(frame.frame_length, b"\x05")
        self.assertEqual(frame.unit_identifier, b"\x00")
        self.assertEqual(frame.function_code, b"\x01")
        self.assertEqual(frame.address, b"\x08\x0C")
        self.assertEqual(frame.data_length, b"\x10")
        self.assertEqual(frame.data, b"")
        self.assertEqual(frame.control_sum, b"\x2A")
        self.assertTrue(frame.is_ok())

    def test_frame_current_params_response(self):
        frame = parse_data(
                start_byte=START_BYTE,
                unit_identifier=UnitIdentifier.RESPONSE,
                function_code=FunctionCodes.VIRTUAL_READ,
                procedure_address=ProcedureAdresses.CURRENT_PARAMS,
                expected_length=ExpectedLength.CURRENT_PARAMS,
                data=b"k\x01w\x00u\x01\xb9\x01\xc8\x00\x95\x01\xc8\x00k\x01",
            )
        self.assertEqual(
            frame.frame_sequence,
            b"A\x15\x01\x01\x08\x0c\x10k\x01w\x00u\x01\xb9\x01\xc8\x00\x95\x01\xc8\x00k\x01\xe0",
        )
        self.assertEqual(frame.start_byte, b"\x41")
        self.assertEqual(frame.frame_length, b"\x15")
        self.assertEqual(frame.unit_identifier, b"\x01")
        self.assertEqual(frame.function_code, b"\x01")
        self.assertEqual(frame.address, b"\x08\x0C")
        self.assertEqual(frame.data_length, b"\x10")
        self.assertEqual(
            frame.data, b"k\x01w\x00u\x01\xb9\x01\xc8\x00\x95\x01\xc8\x00k\x01"
        )
        self.assertEqual(frame.control_sum, b"\xe0")
        self.assertTrue(frame.is_ok())
