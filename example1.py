"""
Sample Code for Lab1
Use "run.py [--sim] lab1" to execute
"""


class Run:
    def __init__(self, factory):
        """Constructor.

        Args:
            factory (factory.FactoryCreate)
        """
        self.create = factory.create_create()
        self.time = factory.create_time_helper()

    def run(self):
        self.create.start()
        self.create.safe()

        self.create.drive_direct(100, 100)
        self.time.sleep(10)
        self.create.drive_direct(0, 0)

        self.create.stop()
