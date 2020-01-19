import unittest
from test_hashing import TestHashing
from test_analysis import TestAnalysis
from test_processing import TestProcessing
from test_similarity import TestSimilarity

if __name__ == '__main__':

    # create list of test classes to run
    TEST_CLASSES = [TestHashing, TestAnalysis, TestProcessing, TestSimilarity]
    TEST_LOADER = unittest.TestLoader()
    TEST_SUITES = []

    # create a list of tests
    for test_class in TEST_CLASSES:
        suite = TEST_LOADER.loadTestsFromTestCase(test_class)
        TEST_SUITES.append(suite)

    # create test suite
    BIG_SUITE = unittest.TestSuite(TEST_SUITES)

    # create test runner and run all the tests in test suite
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_RESULTS = TEST_RUNNER.run(BIG_SUITE)
