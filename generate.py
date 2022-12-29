import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = height / 2
init_z = z
init_height = height
factor = 0.9

pyrosim.Start_SDF("boxes.sdf")
for i in range(5):
    for j in range(5):
        for k in range(10):
            mult = factor**k
            pyrosim.Send_Cube(name="Box-" + str(i) + "," + str(j) + "," + str(k), pos=[x, y, z], size=[length*mult, width*mult, height])
            z += height / 2
            height *= 0.9
            z += height / 2
        height = init_height
        z = init_z
        y += width
    height = init_height
    z = init_z
    y = 0
    x += length
pyrosim.End()
