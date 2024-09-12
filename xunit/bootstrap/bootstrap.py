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
        super().__init__(test_to_run)

    def test_method(self):
        self.log = self.log + "test_method_OK|"

    def setup(self):
        self.log = "setup_OK|"
        


class TestCaseTest(TestCase):
    def __init__(self, test_to_run):
        self.test: Optional[WasRun] = None
        super().__init__(test_to_run)

    def setup(self):
        self.test = WasRun("test_method")

    def test_template_method(self):
        self.test.run()
        assert "setup_OK|test_method_OK|"  == self.test.log



TestCaseTest("test_template_method").run()
