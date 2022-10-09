import unittest

from protokoll300.frame import Frame

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class TestFrame(unittest.TestCase):
    def test_frame_checksum(self):
        frame = Frame("41 05 00 01 08 0C 10 2A")
        self.assertEqual(frame.checksum, b"\x2A")
