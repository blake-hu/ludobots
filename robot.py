import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.robotId = pyb.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.motors = {}

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            print("sensor loaded for: " + linkName)

    def Sense(self, step):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(step)
