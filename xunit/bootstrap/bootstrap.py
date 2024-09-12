from typing import Optional

class TestCase:
    def __init__(self, test_to_run):
        self.test_to_run: str = test_to_run

    def setup(self):
        # this is empty to calls from all TestCaseTest instances keeping run simple.
        pass

    def tear_down(self):
        # this is empty to calls from all TestCaseTest instances keeping run simple.
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        run_test_passed_to_this_test_case = getattr(self, self.test_to_run)
        run_test_passed_to_this_test_case()
        self.tear_down()
        return result


class WasRun(TestCase):
    def __init__(self, test_to_run):
        self.log = None
        super().__init__(test_to_run)

    def setup(self):
        self.log = "setup_OK|"

    def test_method(self):
        self.log = self.log + "test_method_OK|"

    def tear_down(self):
        self.log = self.log + "tear_down_OK|"

    def test_broken_method(self):
        raise Exception

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

class TestResult:
    def __init__(self):
        self.run_count: int = 0

    def test_started(self):
        self.run_count = self.run_count + 1

    def summary(self):
        return f"{self.run_count} run, 0 failed"
    
# Bootstrap tests
TestCaseTest("test_passed_to_this_test_case").run()
TestCaseTest("test_result").run()
# TestCaseTest("test_failed_result").run()