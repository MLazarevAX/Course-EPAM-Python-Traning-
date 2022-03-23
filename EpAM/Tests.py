import unittest
from EpAM.myrange import Myrange

class TestEpamEx(unittest.TestCase):
    def test_my_range(self):
        self.assertEqual(list(Myrange(1, 2)), [1])
