from protokoll300 import utils

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test_isolate_frame():
    assert utils.isolate_frame(b"\x41", b"\x41") == b"\x41"
    assert utils.isolate_frame(b"\x41\x03\x67", b"\x41") == b"\x41\x03\x67"
    assert utils.isolate_frame(b"\x04\x41\x03\x67", b"\x41") == b"\x41\x03\x67"
    assert utils.isolate_frame(b"\x04\x41\x41\x03\x67", b"\x41") == b"\x41\x41\x03\x67"
