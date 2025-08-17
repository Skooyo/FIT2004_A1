from approach3 import intercept
import unittest

class TestIntercept:

    def __init__(self, roads, stations, start, friend_start, expected):
        self.roads = roads
        self.stations = stations
        self.start = start
        self.friend_start = friend_start
        self.expected = expected

    def test(self):
        result = intercept(self.roads, self.stations, self.start, self.friend_start) == self.expected
        print("-------final output for test case:------",
              (intercept(self.roads, self.stations, self.start, self.friend_start)))
        return result


def test_intercept():
    tests = [
        # example 1, Simple
        TestIntercept(
            roads=[(6, 0, 3, 1), (6, 7, 4, 3), (6, 5, 6, 2), (5, 7, 10, 5), (4, 8, 8, 5), (5, 4, 8, 2),
                   (8, 9, 1, 2), (7, 8, 1, 3), (8, 3, 2, 3), (1, 10, 5, 4), (0, 1, 10, 3), (10, 2, 7, 2),
                   (3, 2, 15, 2), (9, 3, 2, 2), (2, 4, 10, 5)],
            stations=[(0, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)],
            start=6,
            friend_start=0,
            expected=(7, 9, [6, 7, 8, 3])
        ),

        # example 2, Unsolvable
        TestIntercept(
            roads=[(0, 1, 35, 3), (1, 2, 5, 2), (2, 0, 35, 4), (0, 4, 10, 1), (4, 1, 22, 2),
                   (1, 5, 65, 1), (5, 2, 70, 1), (2, 3, 10, 1), (3, 0, 20, 3)],
            stations=[(4, 3), (5, 2), (3, 4)],
            start=0,
            friend_start=4,
            expected=None
        ),

        # example 3, Repeated Locations
        TestIntercept(
            roads=[(0, 1, 35, 7), (1, 2, 5, 4), (2, 0, 35, 6), (0, 4, 10, 5), (4, 1, 22, 3),
                   (1, 5, 60, 4), (5, 3, 70, 2), (3, 0, 10, 7)],
            stations=[(4, 2), (5, 1), (3, 4)],
            start=0,
            friend_start=3,
            expected=(160, 39, [0, 1, 2, 0, 1, 2, 0, 4])
        ),

        # example 4, Multiple routes with same cost but different total time
        TestIntercept(
            roads=[(0, 1, 10, 7), (0, 2, 10, 3), (2, 0, 1, 4), (1, 0, 1, 7)],
            stations=[(2, 4), (1, 3)],
            start=0,
            friend_start=1,
            expected=(10, 3, [0, 2])
        ),
        # example 5, mini boss
        TestIntercept(
            roads=[(1, 2, 1, 10), (2, 1, 1, 10), (2, 3, 1, 10), (2, 4, 1, 10)],
            stations=[(3, 55), (4, 55)],
            start=2,
            friend_start=3,
            expected=(11, 110, [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3])
        ),
        # example 6, final boss 
        TestIntercept(
            roads=[(0, 1, 1, 1), (1, 0, 1, 1), (1, 2, 1, 1), (1, 3, 1, 1)],
            stations=[(2, 5), (3, 5)],
            start=1,
            friend_start=2,
            expected=(5, 5, [1, 0, 1, 0, 1, 3])
        ),
        # example 7, Lunatic
        TestIntercept(
            roads=[(0, 1, 1, 1), (1, 0, 1, 1), (1, 2, 1, 1), (2, 1, 1, 1), (0, 2, 1, 1), (2, 0, 1, 1), (0, 3, 1, 1),
                   (3, 0, 1, 1), (1, 3, 1, 1), (3, 1, 1, 1), (2, 3, 1, 1), (3, 2, 1, 1), (0, 4, 1, 1), (0, 5, 1, 1),
                   (1, 4, 1, 1), (1, 5, 1, 1), (2, 4, 1, 1), (2, 5, 1, 1), (3, 4, 1, 1), (3, 5, 1, 1), ],
            stations=[(4, 5), (5, 5)],
            start=0,
            friend_start=4,
            expected=(5, 5, [0, 1, 3, 1, 2, 5])
        )

    ]

    failures = []
    for i, test in enumerate(tests):
        if not test.test():
            failures.append(f"Test case {i + 1} failed")

    if failures:
        for failure in failures:
            print(failure)
        raise AssertionError("Some tests failed")


if __name__ == "__main__":
    # run the tests
    test_intercept()