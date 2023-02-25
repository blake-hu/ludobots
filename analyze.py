import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("./data/backLegSensorValues.npy")
frontLegSensorValues = np.load("./data/frontLegSensorValues.npy")
plt.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
plt.plot(backLegSensorValues, label="Back Leg")
plt.legend()
plt.show()
