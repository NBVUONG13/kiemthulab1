import unittest
from sample import kiem_tra_so_chan

class TestPath(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(kiem_tra_so_chan([]), 0)

    def test_no_even(self):
        self.assertEqual(kiem_tra_so_chan([1, 3, 5]), 0)

    def test_all_even(self):
        self.assertEqual(kiem_tra_so_chan([2, 4, 6]), 3)

if __name__ == '__main__':
    unittest.main()