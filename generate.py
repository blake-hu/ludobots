import pyrosim.pyrosim as pyrosim
import random

scale = 1
length = scale
width = scale
height = scale


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[2, 2, height/2], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    Generate_Body()
    Generate_Brain()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[
                      0, 0, height*1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                       child="BackLeg", type="revolute", position=[-length/2, 0, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                       child="FrontLeg", type="revolute", position=[length/2, 0, height])
    pyrosim.Send_Cube(name="BackLeg", pos=[
                      -length/2, 0, -height/2], size=[length, width, height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[
                      length/2, 0, -height/2], size=[length, width, height])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    for sensorName in range(3):
        for motorName in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName=sensorName,
                                 targetNeuronName=motorName, weight=random.random() * 2 - 1)
    pyrosim.End()


if __name__ == "__main__":
    Create_World()
    Create_Robot()
