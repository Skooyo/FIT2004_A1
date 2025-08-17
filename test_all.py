import unittest
import sys
import os

# Import all test modules
from tests.test import TestOneEd, TestTwoEd, TestRubric, TestScreenshot, TestAdditionalInterceptCases
from tests.more_test import TestOneEd as MoreTestOneEd, TestTwoEd as MoreTestTwoEd, TestRubric as MoreTestRubric
from tests.more_test import TestAdditionalInterceptCases as MoreTestAdditionalInterceptCases
from tests.more_test import TestInterceptEdgeCases, TestAdditionalInterceptions
from tests.more_test import EricTestCase as MoreEricTestCase
from tests.eric_test import EricTestCase
from tests.heap_test import SkooyTestCases


def run_all_tests():
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add all test classes from test.py
    test_suite.addTest(unittest.makeSuite(TestOneEd))
    test_suite.addTest(unittest.makeSuite(TestTwoEd))
    test_suite.addTest(unittest.makeSuite(TestRubric))
    test_suite.addTest(unittest.makeSuite(TestScreenshot))
    test_suite.addTest(unittest.makeSuite(TestAdditionalInterceptCases))
    
    # Add all test classes from more_test.py
    test_suite.addTest(unittest.makeSuite(MoreTestOneEd))
    test_suite.addTest(unittest.makeSuite(MoreTestTwoEd))
    test_suite.addTest(unittest.makeSuite(MoreTestRubric))
    test_suite.addTest(unittest.makeSuite(MoreTestAdditionalInterceptCases))
    test_suite.addTest(unittest.makeSuite(TestInterceptEdgeCases))
    test_suite.addTest(unittest.makeSuite(TestAdditionalInterceptions))
    test_suite.addTest(unittest.makeSuite(MoreEricTestCase))
    
    # Add all test classes from eric_test.py
    test_suite.addTest(unittest.makeSuite(EricTestCase))
    
    # Add SkooyTestCases from heap_test.py
    test_suite.addTest(unittest.makeSuite(SkooyTestCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
    
    print("All tests completed.")

if __name__ == '__main__':
    run_all_tests()
