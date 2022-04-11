
class Engine:

    def get_horsepower():
        return 150

class Transmission:
    pass

class Drivetrain:
    pass

class Car:

    def __init__(self):
        self._engine = Engine()
        self._transmission = Transmission()
        self._drivetrain = Drivetrain()

    def get_horsepower(self):
        return self._engine.get_horsepower()