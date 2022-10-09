import unittest

from protokoll300 import utils


class TestUtils(unittest.TestCase):
    def test_isolate_frame_only_start_byte(self):
        self.assertEqual(
            utils.isolate_frame(b"\x41", b"\x41"),
            b"\x41",
        )

    def test_isolate_frame_starting_with_start_byte(self):
        self.assertEqual(
            utils.isolate_frame(b"\x41\x03\x67", b"\x41"),
            b"\x41\x03\x67",
        )

    def test_isolate_frame_starting_with_diff_byte(self):
        self.assertEqual(
            utils.isolate_frame(b"\x04\x41\x03\x67", b"\x41"),
            b"\x41\x03\x67",
        )

    def test_isolate_frame_double_start_byte(self):
        self.assertEqual(
            utils.isolate_frame(b"\x04\x41\x41\x03\x67", b"\x41"),
            b"\x41\x41\x03\x67",
        )

    def test_isolate_frame_utf8_encoding(self):
        self.assertEqual(
            utils.isolate_frame(
                b"\x06A\x15\x01\x01\x08\x0c\x10\xbf\x01\x97\x00X\x02\xc4\x01\xc8\x00+\x02\xc8\x00\xbf\x01.",
                b"\x41",
            ),
            b"A\x15\x01\x01\x08\x0c\x10\xbf\x01\x97\x00X\x02\xc4\x01\xc8\x00+\x02\xc8\x00\xbf\x01.",
        )


if __name__ == "__main__":
    unittest.main()
