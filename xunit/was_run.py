from test_case import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.was_run: boolean = False
        super().__init__(name)

    def test_method(self):
        self.was_run = True


test = WasRun("test_method")
print(test.was_run)
test.run()
print(test.was_run)
