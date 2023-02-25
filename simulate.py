import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data
import numpy as np
import time as time
import random
# import matplotlib.pyplot as plt

import constants as c
from simulation import SIMULATION


simulation = SIMULATION()


def simulate():
    pass
    # physicsClient = pyb.connect(pyb.GUI)
    # pyb.setAdditionalSearchPath(pybullet_data.getDataPath())
    # planeId = pyb.loadURDF("plane.urdf")
    # robotId = pyb.loadURDF("body.urdf")
    # pyb.loadSDF("world.sdf")

    # pyb.setGravity(0, 0, c.gravity)

    # print("Simulating for " + str(c.duration) + " seconds")

    # pyrosim.Prepare_To_Simulate(robotId)
    # frontLegSensorValues = np.zeros(c.steps)
    # backLegSensorValues = np.zeros(c.steps)

    # for i in range(c.steps):
    #     pyb.stepSimulation()
    #     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
    #         "FrontLeg")
    #     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
    #         "BackLeg")
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex=robotId,
    #         jointName="Torso_BackLeg",
    #         controlMode=pyb.POSITION_CONTROL,
    #         targetPosition=c.frontLegCommand[i % c.num_gridpoints],
    #         maxForce=50,
    #     )
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex=robotId,
    #         jointName="Torso_FrontLeg",
    #         controlMode=pyb.POSITION_CONTROL,
    #         targetPosition=c.backLegCommand[i % c.num_gridpoints],
    #         maxForce=50,
    #     )

    #     if i % 100 == 0:
    #         print("Time elapsed: " + str(i/100) + "s")
    #     time.sleep(0.001)

    # np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
    # np.save("./data/backLegSensorValues.npy", backLegSensorValues)
    # pyb.disconnect()


if __name__ == "__main__":
    simulate()
