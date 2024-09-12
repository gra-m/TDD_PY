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
        # result.test_started() # added without explanation
        self.setup()
        run_test_passed_to_this_test_case = getattr(self, self.test_to_run)
        run_test_passed_to_this_test_case()
        self.tear_down()


class WasRun(TestCase):
    def __init__(self, test_to_run):
        self.log = None
        super().__init__(test_to_run)

    def setup(self):
        # insert set up steps here
        self.log = "setup_OK|"

    def test_method(self):
        # run tests here
        self.log = self.log + "test_method_OK|"

    def tear_down(self):
        self.log = self.log + "tear_down_OK|"

class TestCaseTest(TestCase):
    def __init__(self, test_to_run):
        self.test: Optional[WasRun] = None
        super().__init__(test_to_run)

    def test_passed_to_this_test_case(self):
        self.test = WasRun("test_method")
        self.test.run()
        # runs silent == no output pass tracepoint can be run in debug
        assert "setup_OK|test_method_OK|tear_down_OK|"  == self.test.log



TestCaseTest("test_passed_to_this_test_case").run()
