import pybullet as p
import pybullet_data
import time as time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

p.setGravity(0, 0, -9.8)

for i in range(10000):
	p.stepSimulation()
	print("step: " + str(i))
	time.sleep(0.001)

p.disconnect()
