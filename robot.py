from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.sensor = SENSOR()
        self.motor = MOTOR()
