import unittest

from protokoll300.frame import Frame

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class TestFrame(unittest.TestCase):
    def test_frame_current_params_request(self):
        frame = Frame(b"\x41\x05\x00\x01\x08\x0C\x10\x2A")
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
        frame = Frame(
            b"\x41\x15\x01\x01\x08\x0c\x10\x6c\x01\x7b\x00\x1d\x01\xc6\x01\xc8\x00\x4f\x01\xc8\x00\x6d\x01\x56"
        )
        self.assertEqual(frame.start_byte, b"\x41")
        self.assertEqual(frame.frame_length, b"\x15")
        self.assertEqual(frame.unit_identifier, b"\x01")
        self.assertEqual(frame.function_code, b"\x01")
        self.assertEqual(frame.address, b"\x08\x0C")
        self.assertEqual(frame.data_length, b"\x10")
        self.assertEqual(
            frame.data,
            b"\x6c\x01\x7b\x00\x1d\x01\xc6\x01\xc8\x00\x4f\x01\xc8\x00\x6d\x01",
        )
        self.assertEqual(frame.control_sum, b"\x56")
        self.assertTrue(frame.is_ok())

    def test_frame_outdoor_temp_request(self):
        frame = Frame(b"\x41\x05\x00\x01\x55\x25\x04\x84")
        self.assertEqual(frame.control_sum, b"\x84")
        self.assertEqual(
            frame.data,
            b"",
        )
        self.assertTrue(frame.is_ok())

    def test_frame_too_short(self):
        self.assertRaises(AssertionError, Frame, b"\x41\x05\x00\x01\x55\x25\x84")
