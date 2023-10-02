import random
import numpy as np
from matplotlib import pyplot as plt

num_coordinates = 5000


def f(x):
    return 1 / (1 + x**2)


coordinates_x = np.random.uniform(0, 1, num_coordinates)
coordinates_y = f(coordinates_x)

integral = np.sum(coordinates_y) / num_coordinates

print(integral)

plt.scatter(coordinates_x, coordinates_y, s=10)
