from approach3 import intercept
import unittest

class TestOneEd(unittest.TestCase):
    def test_1(self):
        roads = [(0, 2, 10, 3), (1, 2, 5, 2), (2, 1, 15, 5), (2, 0, 12, 10)]
        stations = [(0, 5), (1, 5)]
        start = 2
        friendStart = 0
        expected_output = (12, 10, [2, 0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_2(self):
        stations_input = [(i, 2) for i in range(20)]
        start_input = 20
        friendStart_input = 0
        roads_input = [(20, 2, 7, 4), (20, 18, 30, 36)] + \
                      [(i, (i+1) % 20, 1, 2) for i in range(20)]
        expected_output = (7, 4, [20, 2])
        result = intercept(roads_input, stations_input, start_input, friendStart_input)
        self.assertEqual(result, expected_output)

    def test_3(self):
        stations_input = [(i, 5) for i in range(20)]
        start_input = 20
        friendStart_input = 0
        roads_input = [(20, 5, 30, 25), (20, 0, 40, 100)] + \
                      [(i, (i+1) % 20, 1, 1) for i in range(20)]
        expected_output = (30, 25, [20, 5])
        result = intercept(roads_input, stations_input, start_input, friendStart_input)
        self.assertEqual(result, expected_output)

    def test_4(self):
        roads = [(0, 1, 1, 1), (1, 0, 1, 1),
                 (2, 3, 1, 1), (3, 2, 1, 1)]
        stations = [(0, 5), (1, 5)]
        start = 2
        friendStart = 0
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test_5(self):
        roads = [(0, 1, 10, 3), (1, 2, 20, 10), (2, 0, 8, 4)]
        stations = [(0, 5), (1, 5), (2, 5)]
        start = 1
        friendStart = 0
        expected_output = (20, 10, [1, 2])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)


class TestTwoEd(unittest.TestCase):
    def test_case_set2(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        stations = [(4, 3), (5, 3), (6, 3)]
        start = 1
        friendStart = 6
        roads = [None] * len(a)

        for number in a:
            roads[number - 1] = [
                (1, 2, 1, 3), (2, 3, 1, 3), (3, 1, 1, 3),
                (1, 4, 1, number), (4, 5, 1, 3), (5, 6, 1, 3), (6, 4, 1, 3)
            ]

        self.assertIsNone(intercept(roads[0], stations, start, friendStart))
        self.assertIsNone(intercept(roads[1], stations, start, friendStart))
        self.assertEqual(intercept(roads[2], stations, start, friendStart), (1, 3, [1, 4]))
        self.assertIsNone(intercept(roads[3], stations, start, friendStart))
        self.assertIsNone(intercept(roads[4], stations, start, friendStart))
        self.assertIsNone(intercept(roads[5], stations, start, friendStart))
        self.assertIsNone(intercept(roads[6], stations, start, friendStart))
        self.assertIsNone(intercept(roads[7], stations, start, friendStart))
        self.assertIsNone(intercept(roads[8], stations, start, friendStart))
        self.assertIsNone(intercept(roads[9], stations, start, friendStart))
        self.assertIsNone(intercept(roads[10], stations, start, friendStart))
        self.assertEqual(intercept(roads[11], stations, start, friendStart), (1, 12, [1, 4]))


class TestRubric(unittest.TestCase):
    def test_example_1(self):
        roads = [
            (6, 0, 3, 1), (6, 7, 4, 3), (6, 5, 6, 2), (5, 7, 10, 5), (4, 8, 8, 5),
            (5, 4, 8, 2), (8, 9, 1, 2), (7, 8, 1, 3), (8, 3, 2, 3), (1, 10, 5, 4),
            (0, 1, 10, 3), (10, 2, 7, 2), (3, 2, 15, 2), (9, 3, 2, 2), (2, 4, 10, 5)
        ]
        stations = [(0, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]
        start = 6
        friendStart = 0
        expected_output = (7, 9, [6, 7, 8, 3])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        roads = [
            (0, 1, 35, 3), (1, 2, 5, 2), (2, 0, 35, 4), (0, 4, 10, 1), (4, 1, 22, 2),
            (1, 5, 65, 1), (5, 2, 70, 1), (2, 3, 10, 1), (3, 0, 20, 3)
        ]
        stations = [(4, 3), (5, 2), (3, 4)]
        start = 0
        friendStart = 4
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test_example_3(self):
        roads = [
            (0, 1, 35, 7), (1, 2, 5, 4), (2, 0, 35, 6), (0, 4, 10, 5), (4, 1, 22, 3),
            (1, 5, 60, 4), (5, 3, 70, 2), (3, 0, 10, 7)
        ]
        stations = [(4, 2), (5, 1), (3, 4)]
        start = 0
        friendStart = 3
        expected_output = (160, 39, [0, 1, 2, 0, 1, 2, 0, 4])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_example_4(self):
        roads = [
            (0, 1, 10, 7), (0, 2, 10, 3), (2, 0, 1, 4), (1, 0, 1, 7)
        ]
        stations = [(2, 4), (1, 3)]
        start = 0
        friendStart = 1
        expected_output = (10, 3, [0, 2])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)
        
    def test_miniloop(self):
        roads = [(0, 1, 20, 3), (1, 2, 10, 2), (2, 0, 15, 4), (0, 3, 50, 2), (3, 4, 10, 1), (4, 5, 10, 1), (5, 6, 10, 1), (6, 1, 30, 2)]
        stations = [(3, 2), (6, 1), (1, 4)]   
        start = 0
        friendStart = 6
        self.assertEqual(intercept(roads, stations, start, friendStart), (125, 14, [0, 1, 2, 0, 3, 4, 5, 6]))
        
        
    def test_linear_path(self):
        """
        * A straight path, driver must travel along a linear road 0->1->2->3->4
        
        ! There is also a bad shortcut from 1->4 which will give too high of a
        ! cost, even though it has a time of 0 to travel.
        !  The driver should skip this "bad shortcut".
        """
        roads = [(0,1,5,2), (1,2,5,2), (2,3,5,2), (3,4,5,2), (1,4,30,2)]
        stations = [(4,2), (2,2)]
        start = 0
        friend_start = 4
        
        self.assertEqual(intercept(roads, stations, start, friend_start), 
                         (20, 8, [0,1,2,3,4]))

    def test_branch_choice(self):
        """
        * Need to choose between two paths, one clearly better than the other
        
        ! The driver must choose to take the shortcut from 1->4.
        ! This shortcut has both better cost & time compared to 1->2->3->4.
        """
        # Need to choose between two paths, one clearly better than the other
        roads = [(0,1,5,2), (1,2,5,2), (2,3,5,2), (3,4,5,2), (1,4,14,2)]
        stations = [(4,2), (2,2)]
        start = 0
        friend_start = 4
        
        self.assertEqual(intercept(roads, stations, start, friend_start), 
                         (19,4,[0,1,4]))

    def test_same_start(self):
        roads = [(0, 1, 5, 1), (1, 2, 5, 1), (2, 0, 5, 1)]
        stations = [(0, 2), (1, 2)]
        start = 0
        friendStart = 0

        self.assertEqual(intercept(roads, stations, start, friendStart), (0, 0, [0]))
        
        
class TestScreenshot(unittest.TestCase):
    def test_screenshot_1(self):
        r = [
            (6, 0, 3, 1), (6, 7, 4, 3), (6, 5, 6, 2), (5, 7, 10, 5),
            (4, 8, 8, 5), (5, 4, 8, 2), (8, 9, 1, 2), (7, 8, 1, 3),
            (8, 3, 2, 3), (1, 10, 5, 4), (0, 1, 10, 3), (10, 2, 7, 2),
            (3, 2, 15, 2), (9, 3, 2, 2), (2, 4, 10, 5)
        ]
        stat = [(0, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]
        start = 6
        start1 = 0
        result = intercept(r, stat, start, start1)

    def test_screenshot_2(self):
        r = [
            (0, 1, 2, 2), (1, 2, 2, 2), (2, 3, 2, 2), (3, 4, 2, 2)
        ]
        stat = [(1, 1), (2, 1), (3, 1), (4, 1), (0, 1)]
        start = 0
        start1 = 2
        result = intercept(r, stat, start, start1)

    def test_screenshot_3(self):
        r = [
            (0, 1, 35, 3), (1, 2, 5, 2), (2, 0, 35, 4), (0, 4, 10, 1), (4, 1, 22, 2),
            (1, 5, 65, 1), (5, 2, 70, 1), (2, 3, 10, 1), (3, 0, 20, 3)
        ]
        stat = [(4, 3), (5, 2), (3, 4)]
        start = 0
        start1 = 4
        result = intercept(r, stat, start, start1)
        
    def test_long_chase(self):
            import sys
            rec_lim = sys.getrecursionlimit()
            sys.setrecursionlimit(2000)
            roads = [(i, i+1, 3, 5) for i in range(19)] + [(19, 0, 3, 4)]
            stations = [(i, 5) for i in range(20)]
            start = 0
            friend_start = 19

            #1900 edges traversed/95 cycles
            self.assertEqual(intercept(roads, stations, start, friend_start), (5700, 9405, [i for i in range(20)]*95+[0]))
            # sys.setrecursionlimit(rec_lim)
      

class TestAdditionalInterceptCases(unittest.TestCase):

    def test1(self):
        roads = []
        stations = [(0, 5), (1, 5)]
        start = 0
        friendStart = 0
        output = (0, 0, [0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, output)

    def test2(self):
        roads = [
            (0, 1, 1, 3), (0, 2, 1, 5), (1, 3, 2, 3), (2, 3, 2, 2)
        ]
        stations = [(3, 2), (0, 2)]
        start = 0
        friendStart = 3
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test3(self):
        roads = [(0, 1, 5, 5)]
        stations = [(1, 3), (0, 3)]
        start = 0
        friendStart = 1
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test4(self):
        roads = [(0, 1, 2, 2), (1, 2, 2, 2), (2, 0, 2, 2)]
        stations = [(2, 3), (0, 3)]
        start = 0
        friendStart = 0
        output = (0, 0, [0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, output)

    def test5(self):
        roads = [(0, 1, 2, 2)]
        stations = [(3, 1), (4, 1)]
        start = 0
        friendStart = 3
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test6(self):
        roads = [(0, 1, 2, 2), (1, 2, 2, 2)]
        stations = [(5, 2), (6, 2)]
        start = 0
        friendStart = 5
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test7(self):
        roads = [(0, 1, 2, 2)]
        stations = [(1, 5), (0, 5)]
        start = 0
        friendStart = 1
        result = intercept(roads, stations, start, friendStart)
        self.assertIsNone(result)

    def test8(self):
        roads = [(0, 1, 3, 6)]
        stations = [(1, 2), (2, 2), (0, 2)]
        start = 0
        friendStart = 1
        output = (3, 6, [0, 1])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, output)

    def test9(self):
        roads = [
            (0, 1, 2, 2), (1, 2, 3, 2), (2, 3, 1, 2), (3, 4, 2, 4), (4, 5, 1, 5),
            (0, 6, 10, 4), (6, 7, 1, 1), (7, 8, 1, 1), (8, 5, 1, 1),
            (1, 9, 5, 2), (9, 10, 2, 1), (10, 5, 2, 1),
            (2, 11, 3, 1), (11, 12, 2, 1), (12, 13, 3, 1), (13, 5, 4, 1),
            (3, 14, 2, 1), (14, 5, 2, 1), (0, 10, 20, 6), (6, 12, 15, 4)
        ]
        stations = [(5, 3), (13, 3), (10, 3), (0, 3), (1, 3)]
        start = 0
        friendStart = 5

        output = (9, 15, [0, 1, 2, 3, 4, 5])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, output)

def run_tests():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
