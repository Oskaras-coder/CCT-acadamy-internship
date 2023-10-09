import unittest
import task3_extended
from parameterized import parameterized


class TestAddition(unittest.TestCase):
    @parameterized.expand([(100, {10: 100, 20: 1, 50: 1}, [50, 20, 10, 10, 10]),
                           (13, {1: 10, 2: 1, 5: 5}, [5, 5, 2, 1]),
                           (13, {1: 10, 2: 1, 5: 1}, [5, 2, 1, 1, 1, 1, 1, 1]),
                           (11, {2: 4, 5: 2}, [5, 2, 2, 2]),
                           (117, {2: 3, 5: 4, 10: 1, 100: 20}, [100, 10, 5, 2]),
                           (167, {1: 10, 2: 4, 5: 7, 50: 2, 100: 2}, [100, 50, 5, 5, 5, 2]),
                           (13, {2: 30, 10: 70}, False),
                           (13.5, {2: 20, 10: 5}, False),
                           (130.5, {0.5: 4, 10: 15, 20: 14, 50: 2}, [50, 50, 20, 10, 0.5]),
                           (1.5, {0.1: 3, 0.2: 10}, [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1]),
                           (1.5, {0.1: 3, 0.2: 10, 0.5: 1}, [0.5, 0.2, 0.2, 0.2, 0.2, 0.2]),
                           (0.77, {0.01: 10, 0.05: 3, 0.1: 2, 0.2: 6}, [0.2, 0.2, 0.2, 0.1, 0.05, 0.01, 0.01]),
                           (100, {10: 100, 20: 1, 50: 1}, [50, 20, 10, 10, 10]),
                           (1, {10: 100}, False)
                           ])
    def test_split_amount(self, amount, banknotes_test, expected):
        self.assertEqual(task3_extended.split_amount(amount=amount, banknotes=banknotes_test), expected)
