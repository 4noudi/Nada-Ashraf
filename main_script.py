import unittest

DEBUG = True

if __name__ == "__main__":

    if DEBUG:
        import logging
        logging.basicConfig(level=logging.INFO)

    # Discover and run all test modules in the 'tests' folder
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")

    # Run the test suite
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    # Exit with an appropriate exit code based on the test results
    exit_code = 0 if result.wasSuccessful() else 1
    exit(exit_code)
