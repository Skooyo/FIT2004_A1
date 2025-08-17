from approach3 import intercept
import unittest

class EricTestCase(unittest.TestCase):
    def test_case2_multiple_stations_trick1(self):
        roads = [
            (0, 4, 1, 1),
            (4, 1, 1, 3),
            (1, 7, 2, 5),  
            (0, 1, 3, 4),
            (1, 2, 2, 2),
            (2, 7, 1, 4),
            (0, 3, 2, 3),
            (3, 5, 2, 6)
        ]
        stations = [(2, 1), (5, 3), (7, 2)]
        start = 0
        friendStart = 5 
        res = intercept(roads, stations, start, friendStart)
        expected_output = (4, 9, [0, 4, 1, 7])
        self.assertIsNotNone(expected_output, res)
    
    def test_case3_direct_interception(self):
        roads = [
            (0, 9, 4, 5),
            (0, 3, 2, 2),
            (3, 9, 10, 3),
            (0, 1, 1, 1),
            (1, 2, 2, 2),
            (2, 8, 1, 3),
            (8, 9, 2, 1),
            (0, 4, 3, 2),
            (4, 9, 1, 3)
        ]
        stations = [(2, 3), (4, 2), (6, 4), (7, 5), (9, 1)]
        start = 0
        friendStart = 7  
        res = intercept(roads, stations, start, friendStart)
        expected_output = (4, 5, [0, 9])
        self.assertIsNotNone(expected_output, res)
    
    def test_case4_late_cycle_interception(self):
        roads = [
            (0, 1, 2, 4),
            (1, 3, 2, 3),
            (3, 5, 4, 4),
            (5, 9, 3, 9), 
            (0, 2, 3, 3),
            (2, 9, 2, 4)
        ]
        stations = [(2, 5), (8, 5), (9, 5)]
        start = 0
        friendStart = 8
        
        expected_output = (11, 20, [0, 1, 3, 5, 9])
        res = intercept(roads, stations, start, friendStart)
        self.assertEqual(res, expected_output)
    
    def test_case5_max_station_cycle(self):
        stations = [
            (10, 1), (11, 2), (12, 3), (13, 4), (14, 5),
            (15, 1), (16, 2), (17, 3), (18, 4), (19, 5),
            (20, 1), (21, 2), (22, 3), (23, 4), (24, 5),
            (25, 1), (26, 2), (27, 3), (28, 4), (29, 5)
        ]
        roads = [
            (0, 29, 7, 15), 
            (0, 2, 3, 7),
            (2, 29, 2, 8), 
            (0, 10, 6, 16),
            (10, 11, 1, 2),
            (11, 12, 1, 2)
        ]
        start = 0
        friendStart = 24
        res = intercept(roads, stations, start, friendStart)
        expected_output = (5, 15, [0, 2, 29])
        self.assertEqual(expected_output, res)
    
    def test_case6_multiple_candidate_paths(self):
        roads = [
            (0, 2, 2, 4),
            (2, 7, 1, 5),
            (0, 1, 4, 6),
            (1, 3, 0, 4),
            (0, 4, 10, 3),
            (4, 7, 0, 6)
        ]
        stations = [(3,2), (5,3), (7,1)]
        start = 0
        friendStart = 5
        res = intercept(roads, stations, start, friendStart)
        expected_output = (3, 9, [0, 2, 7])
        self.assertEqual(expected_output, res)


def run_tests():
    unittest.main()