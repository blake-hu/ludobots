import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import numpy as np

import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=pyb.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce,
        )
