import pybullet as p
import time as time

physicsClient = p.connect(p.GUI)
for i in range(1000):
	p.stepSimulation()
	print("step: " + str(i))
	time.sleep(0.01)

p.disconnect()
