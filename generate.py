import pyrosim.pyrosim as pyrosim

scale = 1
length = scale
width = scale
height = scale

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2, 2, height/2], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, height*1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -width/2, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, width/2, height])
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -width/2, -height/2], size=[length, width, height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, width/2, -height/2], size=[length, width, height])
    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()