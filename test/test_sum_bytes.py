import unittest

from protokoll300.utils import sum_bytes_mod_256


class TestUtils(unittest.TestCase):
    def test_sum_one_byte(self):
        self.assertEqual(
            sum_bytes_mod_256(b"\x41"),
            b"\x41",
        )

    def test_sum_two_bytes(self):
        self.assertEqual(
            sum_bytes_mod_256(b"\x41\x01"),
            b"\x42",
        )

    def test_sum_max(self):
        self.assertEqual(
            sum_bytes_mod_256(b"\xFF"),
            b"\xff",
        )

    def test_sum_max_over(self):
        self.assertEqual(
            sum_bytes_mod_256(b"\x06\x01\x01\x37\xd3\x01\x06"),
            b"\x19",
        )
