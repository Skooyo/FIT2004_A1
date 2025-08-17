from approach3 import intercept
import unittest

class SkooyTestCases(unittest.TestCase):
    def test_alot_of_updates(self):
        roads = [(3, 1, 50, 4), (3, 4, 40, 2), (4, 1, 9, 2), (4, 5, 2, 2), (5, 6, 5, 2), (5, 1, 2, 4), (6, 1, 20, 2), (2, 3, 10, 2)]
        stations = [(1, 2), (2, 2)]
        friendStart = 1
        start = 3
        res = intercept(roads, stations, start, friendStart)
        expected_output = (44, 8, [3, 4, 5, 1])
        self.assertEqual(res, expected_output)