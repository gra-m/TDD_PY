class TestCase:
    def __init__(self, test_to_run):
        self.test_to_run: str = test_to_run




class WasRun(TestCase):
    def __init__(self, test_to_run):
        self.was_run: bool = False
        super().__init__(test_to_run)

    def test_method(self):
        self.was_run = True

    def run(self):
        run_test_passed_to_this_test_case = getattr(self, self.test_to_run)
        run_test_passed_to_this_test_case()


test = WasRun("test_method")
print (test.was_run)
test.run()
print (test.was_run)