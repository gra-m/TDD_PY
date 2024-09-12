from typing import Optional


class TestCase:
    def __init__(self, test_to_run):
        self.test_to_run: str = test_to_run

    def setup(self):
        pass

    def run(self):
        self.setup()
        run_test_passed_to_this_test_case = getattr(self, self.test_to_run)
        run_test_passed_to_this_test_case()


class WasRun(TestCase):
    def __init__(self, test_to_run):
        self.log = None
        self.was_run: bool
        super().__init__(test_to_run)

    def test_method(self):
        self.was_run = True
        self.log = self.log + "test_method "

    def setup(self):
        self.was_run = False
        self.log = "setup "
        


class TestCaseTest(TestCase):
    def __init__(self, test_to_run):
        self.test: Optional[WasRun] = None
        super().__init__(test_to_run)

    def setup(self):
        self.test = WasRun("test_method")

    def test_setup(self):
        self.test.run()
        assert "setup test_method "  == self.test.log

    def test_running(self):
        self.test.run()
        assert self.test.was_run


TestCaseTest("test_setup").run()
TestCaseTest("test_running").run()
