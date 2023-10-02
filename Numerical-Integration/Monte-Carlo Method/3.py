import random
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (x**3) / ((np.e)**x - 1)


height = 1.5
width = 10
num_coordinates = 1000000

coordinates_x = np.random.uniform(0, width, num_coordinates)
coordinates_y = np.random.uniform(0, height, num_coordinates)

ns = np.sum(coordinates_y <= f(coordinates_x))

x = np.linspace(0, width, 100)

plt.plot(x, f(x), color='red')

plt.scatter(coordinates_x, coordinates_y, s=1)

area = (height * width * ns) / num_coordinates
print('Area:', area)

plt.show()
