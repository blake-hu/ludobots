import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data
import numpy as np
import time as time
import random

import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = pyb.connect(pyb.GUI)
        pyb.setAdditionalSearchPath(pybullet_data.getDataPath())
        pyb.setGravity(0, 0, c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()

        print("\n——————————————")
        print("Simulating for " + str(c.duration) + " seconds")

    def __del__(self):
        pyb.disconnect()
        print("pybullet simulator disconnected")

    def Run(self):
        for step in range(c.steps):
            pyb.stepSimulation()
            self.robot.Sense(step)
            self.robot.Think()
            self.robot.Act(step)

            if step % 100 == 0:
                print("Time elapsed: " + str(step/100) + "s")
            time.sleep(0.001)

        self.robot.Save_Sensor_Values(c.save_dir)
        print("Saved motor and sensor values")
