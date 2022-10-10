import unittest

from protokoll300.frame import parse_data
from protokoll300.codes import (
    START_BYTE,
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdresses,
    ExpectedLength,
)


class TestUtilsParseData(unittest.TestCase):
    def test_parse_data_outdoor_temp_response(self):

        frame = parse_data(
            start_byte=START_BYTE,
            unit_identifier=UnitIdentifier.RESPONSE,
            function_code=FunctionCodes.VIRTUAL_READ,
            procedure_address=ProcedureAdresses.OUTDOOR_TEMP,
            expected_length=ExpectedLength.OUTDOOR_TEMP,
            data=b"\x8f\x00\x91\x00",
        )

        self.assertEqual(
            frame.frame_sequence,
            b"\x41\x09\x01\x01\x55\x25\x04\x8f\x00\x91\x00\xa9",
        )

    # 41 06 01 01 37 D3 01 06 19
    def test_parse_data_slope_response(self):

        frame = parse_data(
            start_byte=START_BYTE,
            unit_identifier=UnitIdentifier.RESPONSE,
            function_code=FunctionCodes.VIRTUAL_READ,
            procedure_address=ProcedureAdresses.M2_HEATING_CURVE_SLOPE,
            expected_length=ExpectedLength.M2_HEATING_CURVE_SLOPE,
            data=b"\x06",
        )

        self.assertEqual(
            frame.frame_sequence,
            b"A\x06\x01\x01\x37\xd3\x01\x06\x19",
        )
