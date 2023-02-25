import pyrosim.pyrosim as pyrosim
import pybullet
import pybullet_data
import numpy as np
import time as time


def simulate():
    physicsClient = pybullet.connect(pybullet.GUI)
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = pybullet.loadURDF("plane.urdf")
    robotId = pybullet.loadURDF("body.urdf")
    pybullet.loadSDF("world.sdf")

    pybullet.setGravity(0, 0, -9.8)

    duration = 5  # Simulation duration in seconds
    steps = duration * 100
    print("Simulating for " + str(duration) + " seconds")

    pyrosim.Prepare_To_Simulate(robotId)
    frontLegSensorValues = np.zeros(steps)
    backLegSensorValues = np.zeros(steps)

    for i in range(steps):
        pybullet.stepSimulation()
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            "FrontLeg")
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            "BackLeg")

        if i % 100 == 0:
            print("Time elapsed: " + str(i/100) + "s")
        time.sleep(0.001)

    np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
    np.save("./data/backLegSensorValues.npy", backLegSensorValues)
    pybullet.disconnect()


if __name__ == "__main__":
    simulate()
