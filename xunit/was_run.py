from test_case import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.was_run: bool = False
        super().__init__(name)

    def test_method(self):
        self.was_run = True


