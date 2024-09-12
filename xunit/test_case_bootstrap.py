from test_case import TestCase
from was_run import WasRun


class TestCaseBootstrap(TestCase):
    """
    TestCaseBootstrap class is designed to perform a test run
    and verify that the test method was executed.

    Methods
    -------

    run()
        Creates an instance of WasRun with the specified test
        method, ensures the method was not run before execution,
        runs the test, and then asserts that the method was run.
    """
    def run_bootstrap(self):
        test = WasRun("test_method")
        assert(not test.was_run)
        test.run()
        assert test.was_run

TestCaseBootstrap("test_running").run_bootstrap()