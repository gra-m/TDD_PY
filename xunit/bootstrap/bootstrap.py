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
        self.was_run: bool = False
        self.was_setup: bool = False
        super().__init__(test_to_run)

    def test_method(self):
        self.was_run = True

    def setup(self):
        self.was_setup = True


class TestCaseTest(TestCase):
    def __init__(self, test_to_run):
        super().__init__(test_to_run)

    def test_setup(self):
        test = WasRun("test_method")
        test.run()
        assert(test.was_setup)

    def test_running(self):
        test = WasRun("test_method")
        # the asserts only report if they fail, to see output add tracepoints and print(test.was_run) and run in debug.
        assert(not test.was_run)
        test.run()
        assert test.was_run


TestCaseTest("test_setup").run()
TestCaseTest("test_running").run()
