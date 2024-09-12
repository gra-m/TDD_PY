class WasRun:
    def __init__(self, name):
        self.was_run: bool = False

    def test_method(self):
        self.was_run = True


test = WasRun("test_method")
print (test.was_run)
test.test_method()
print (test.was_run)