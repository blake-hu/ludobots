import numpy as np

# For simulation
duration = 3  # Simulation duration in seconds
steps = duration * 100

# For motor control
num_gridpoints = 100
gridpoints = np.linspace(0, 2*np.pi, num_gridpoints)
frontLegCommand = np.sin(gridpoints)*np.pi/4
backLegCommand = np.sin(gridpoints+np.pi/4)*np.pi/4
# plt.plot(frontLegCommand)
# plt.plot(backLegCommand)
# plt.show()
# exit()

gravity = -9.8
