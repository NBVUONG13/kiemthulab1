import unittest
from sample import kiem_tra_so_chan

class TestStatement(unittest.TestCase):
    def test_coverage(self):
        
        self.assertEqual(kiem_tra_so_chan([2]), 1)

if __name__ == '__main__':
    unittest.main()