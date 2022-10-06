from protokoll300.frame import RequestFrame, ResponseFrame, Frame
from protokoll300.codes import (
    UnitIdentifier,
    FunctionCodes,
    ProcedureAdressesAndExpectedLength,
)

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test_frame_checksum():
    frame = Frame("41 05 00 01 08 0C 10 2A")
    assert frame.checksum == 42


def test_request_frame_checksum():
    frame = RequestFrame(
        start_byte=b"\x41",
        unit_identifier=UnitIdentifier.REQUEST.value,
        function_code=FunctionCodes.VIRTUAL_READ.value,
        procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
    )
    assert frame.checksum == 42


def test_request_frame_current_params():
    frame = RequestFrame(
        start_byte=b"\x41",
        unit_identifier=UnitIdentifier.REQUEST.value,
        function_code=FunctionCodes.VIRTUAL_READ.value,
        procedure_adress_and_length=ProcedureAdressesAndExpectedLength.CURRENT_PARAMS.value,
    )
    assert frame.sequence == b"\x41\x05\x00\x01\x08\x0C\x10\x2A"
