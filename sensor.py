import pyrosim.pyrosim as pyrosim
import numpy as np


import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.sensorValues = np.zeros(c.steps)

    def Get_Value(self, step):
        self.sensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            self.linkName)

    def Save_Values(self, dir_path):
        np.save(dir_path + "SensorValue_" + self.linkName, self.sensorValues)
