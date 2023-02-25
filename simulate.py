import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time as time


def simulate():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeId = p.loadURDF("plane.urdf")
    robotId = p.loadURDF("body.urdf")
    p.loadSDF("world.sdf")

    p.setGravity(0, 0, -9.8)

    duration = 100  # Simulation duration in seconds
    print("Simulating for " + str(duration) + " seconds")
    pyrosim.Prepare_To_Simulate(robotId)

    for i in range(duration*100):
        p.stepSimulation()
        backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        print(backLegTouch)

        if i % 100 == 0:
            print("Time elapsed: " + str(i/100) + "s")
        time.sleep(0.001)

    p.disconnect()


if __name__ == "__main__":
    simulate()
