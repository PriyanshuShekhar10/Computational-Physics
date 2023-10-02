import random
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return 1 / (1 + x**2)


height = 1.02
num_coordinates = 1000000

coordinates_x = np.random.uniform(0, 1, num_coordinates)
coordinates_y = np.random.uniform(0, height, num_coordinates)

ns = np.sum(coordinates_y <= f(coordinates_x))

x = np.linspace(0, 1, 100)

plt.plot(x, f(x), color='red')
plt.scatter(coordinates_x, coordinates_y, s=0.1)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

print('ns:', ns)

area = height * ns / num_coordinates
print('Area:', area)

plt.show()
