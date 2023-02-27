import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data

from sensor import SENSOR
from motor import MOTOR
import constants as c


class ROBOT:
    def __init__(self):
        self.robotId = pyb.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            print("sensor loaded for: " + linkName)

    def Sense(self, step):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(step)

    def Save_Sensor_Values(self, dir_path):
        for linkName in self.sensors:
            self.sensors[linkName].Save_Values(dir_path)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            if jointName == "Torso_FrontLeg":
                self.motors[jointName].Prepare_To_Act(
                    c.amplitude, c.frequency*5, c.offset, c.maxForce)
            else:
                self.motors[jointName].Prepare_To_Act(
                    c.amplitude, c.frequency, c.offset, c.maxForce)
            print("motor loaded for: " + jointName)

    def Act(self, step):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(step, self.robotId)

    def Save_Motor_Values(self, dir_path):
        for jointName in self.motors:
            self.motors[jointName].Save_Values(dir_path)
