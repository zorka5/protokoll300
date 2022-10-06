import unittest

from protokoll300 import utils


class TestUtils(unittest.TestCase):
    def test_isolate_frame(self):
        self.assertEqual(
            utils.isolate_frame(b"\x41", b"\x41"),
            b"\x41",
        )
        self.assertEqual(
            utils.isolate_frame(b"\x41\x03\x67", b"\x41"),
            b"\x41\x03\x67",
        )
        self.assertEqual(
            utils.isolate_frame(b"\x04\x41\x03\x67", b"\x41"),
            b"\x41\x03\x67",
        )
        self.assertEqual(
            utils.isolate_frame(b"\x04\x41\x41\x03\x67", b"\x41"),
            b"\x41\x41\x03\x67",
        )
