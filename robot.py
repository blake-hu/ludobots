import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = pyb.loadURDF("body.urdf")
