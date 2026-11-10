import unittest
import github_unittest_ex as gu

class SumTest(unittest.TestCase):

    def test_findMaxSum(self):
        self.assertEqual(gu.findMaxSum(2, 5, 7), 12)
        self.assertEqual(gu.findMaxSum(1, 1, 1), 2)
        self.assertEqual(gu.findMaxSum(-3, 4, -1), 3)
        self.assertEqual(gu.findMaxSum(2, 3, 3), 6)


if __name__ == "__main__":
    unittest.main()