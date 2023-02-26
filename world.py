import pyrosim.pyrosim as pyrosim
import pybullet as pyb
import pybullet_data


class WORLD:
    def __init__(self):
        self.laneId = pyb.loadURDF("plane.urdf")
        pyb.loadSDF("world.sdf")
