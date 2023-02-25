import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data
import numpy as np
import time as time
import random
# import matplotlib.pyplot as plt


def simulate():
    physicsClient = pyb.connect(pyb.GUI)
    pyb.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = pyb.loadURDF("plane.urdf")
    robotId = pyb.loadURDF("body.urdf")
    pyb.loadSDF("world.sdf")

    pyb.setGravity(0, 0, -9.8)

    duration = 10  # Simulation duration in seconds
    steps = duration * 100
    print("Simulating for " + str(duration) + " seconds")

    pyrosim.Prepare_To_Simulate(robotId)
    frontLegSensorValues = np.zeros(steps)
    backLegSensorValues = np.zeros(steps)

    gridpoints = np.linspace(0, 2*np.pi, 100)
    frontLegCommand = np.sin(gridpoints)*np.pi/4
    backLegCommand = np.sin(gridpoints+np.pi/4)*np.pi/4
    # plt.plot(frontLegCommand)
    # plt.plot(backLegCommand)
    # plt.show()
    # exit()

    for i in range(steps):
        pyb.stepSimulation()
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            "FrontLeg")
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            "BackLeg")
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName="Torso_BackLeg",
            controlMode=pyb.POSITION_CONTROL,
            targetPosition=frontLegCommand[i % len(gridpoints)],
            maxForce=50,
        )
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName="Torso_FrontLeg",
            controlMode=pyb.POSITION_CONTROL,
            targetPosition=backLegCommand[i % len(gridpoints)],
            maxForce=50,
        )

        if i % 100 == 0:
            print("Time elapsed: " + str(i/100) + "s")
        time.sleep(0.001)

    np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
    np.save("./data/backLegSensorValues.npy", backLegSensorValues)
    pyb.disconnect()


if __name__ == "__main__":
    simulate()
