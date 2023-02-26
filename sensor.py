import pyrosim.pyrosim as pyrosim
import numpy as np


import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.steps)

    def Get_Value(self, step):
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            self.linkName)
