import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import numpy as np

import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Prepare_To_Act(self, amplitude, frequency, offset, maxForce):
        self.amplitude = amplitude
        self.frequency = frequency
        self.offset = offset
        self.maxForce = maxForce

        # For motor control
        self.num_gridpoints = 100
        self.gridpoints = np.linspace(0, 2*np.pi, self.num_gridpoints)
        self.motorValues = np.sin(
            self.frequency * self.gridpoints + self.offset) * self.amplitude
        # plt.plot(frontLegCommand)
        # plt.plot(backLegCommand)
        # plt.show()
        # exit()

    def Set_Value(self, step, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=pyb.POSITION_CONTROL,
            targetPosition=self.motorValues[step % self.num_gridpoints],
            maxForce=self.maxForce,
        )

    def Save_Values(self, dir_path):
        np.save(dir_path + "MotorValue_" + self.jointName, self.motorValues)
