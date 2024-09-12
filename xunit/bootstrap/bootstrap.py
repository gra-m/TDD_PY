import sys
import traceback
from typing import Optional
import logging

from xunit.bootstrap.unit_testing_helper import TestUtils

logging.basicConfig(level=logging.INFO)

class TestFailedException(Exception):
    pass

class SetupFailedException(Exception):
    pass

class TestCase:
    def __init__(self, test_to_run):
        self.test_to_run: str = test_to_run
        # at present the only way to know tests on this test framework are working is by showing assertion errors
        self.catch_assertion_errors: bool = True
        if self.catch_assertion_errors:
            TestUtils.warning_message("Assertion Errors used to test framework are being ignored with the below:"
                                      "\nself.catch_assertion_errors: bool = True\n")


    def setup(self):
        # this is empty to calls from all TestCaseTest instances keeping run simple.
        pass

    def tear_down(self):
        # this is empty to calls from all TestCaseTest instances keeping run simple.
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        try:
            self.setup() # any exceptions in self setup must prop as setupfailedexceptions independent tests
            run_test_passed_to_this_test_case = getattr(self, self.test_to_run)
            run_test_passed_to_this_test_case()
        except SetupFailedException as e:
            logging.info(f" @: {str(e)}\n Traceback: {traceback.format_exc(0)}")
            result.test_failed()
            self.tear_down()
            return result
        except AssertionError as e:
            if not self.catch_assertion_errors:
                raise TestFailedException(e)
        except TestFailedException as e:    # Not catching Assertion Errors here so can test tests!
            logging.info(f" @: {str(e)}\n Traceback: {traceback.format_exc(0)}")
            result.test_failed()
            self.tear_down()
            return result
        except Exception as e:
            logging.exception(f" @: {str(e)}\n Traceback: {traceback.format_exc(0)}")
            logging.fatal(f" Exiting after caught exception: {e}")
            sys.exit(1)

        self.tear_down()
        return result


class WasRun(TestCase):
    def __init__(self, test_to_run):
        self.log = None
        super().__init__(test_to_run)

    def setup(self):
        # catch any exception/ trace back and propagate as a setupfailedexception
        self.log = "setup_OK|"

    def test_method(self):
        self.log = self.log + "test_method_OK|"

    def tear_down(self):
        self.log = self.log + "tear_down_OK|"

    def test_broken_method(self):
        raise TestFailedException("test_broken_method failed as expected.")

    def test_broken_setup(self):
        raise SetupFailedException("SetupFailed Exception raised as expected.")

class TestCaseTest(TestCase):
    def __init__(self, test_to_run):
        self.test: Optional[WasRun] = None
        super().__init__(test_to_run)

    def test_passed_to_this_test_case(self):
        self.test = WasRun("test_method")
        self.test.run()
        # runs silent == no output pass tracepoint can be run in debug
        assert "setup_OK|test_method_OK|tear_down_OK|"  == self.test.log

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert("1 run, 1 failed" == result.summary())

    def test_setup_exception_caught(self):
            test = WasRun("test_broken_setup")
            TestUtils.assert_raises(SetupFailedException, test.run)


class TestResult:
    def __init__(self):
        self.run_count: int = 0
        self.failure_count: int = 0

    def test_started(self):
        self.run_count = self.run_count + 1

    def test_failed(self):
        self.failure_count = self.failure_count + 1

    def summary(self):
        return f"{self.run_count} run, {self.failure_count} failed"
    
# Bootstrap tests
TestCaseTest("test_passed_to_this_test_case").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result_formatting").run()
TestCaseTest("test_failed_result").run()
TestCaseTest("test_setup_exception_caught").run()