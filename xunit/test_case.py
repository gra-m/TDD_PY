class TestCase:
    def __init__(self, name):
        self.name: String = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
