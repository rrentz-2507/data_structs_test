import unittest
import github_unittest_ex as gu

class SumTest(unittest.TestCase):

    def test_findMaxSum(self):
        self.assertEqual(gu.findMaxSum(2, 5, 7), 12)


if __name__ == "__main__":
    unittest.main()