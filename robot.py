import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
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
        self.nn = NEURAL_NETWORK("brain.nndf")
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

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            print("motor loaded for: " + jointName)

    def Act(self, step):
        for neuronName in self.nn.Get_Neuron_Names().keys():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                print(jointName + " moving to " + str(desiredAngle))
