import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data
import numpy as np
import time as time
import random
# import matplotlib.pyplot as plt

import constants as c
from simulation import SIMULATION


def simulate():
    simulation = SIMULATION()

    np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
    np.save("./data/backLegSensorValues.npy", backLegSensorValues)
    pyb.disconnect()


if __name__ == "__main__":
    simulate()
