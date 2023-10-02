import random
import numpy as np
from matplotlib import pyplot as plt
import math

def f(x):
  # return 1/(1 + x**2)
  return (x**3)/(((math.e)**x) -1)

height = 1.5
width = 10
num_coordinates = 1000
coordinates_x = []
coordinates_y = []
ns = 0

for _ in range(num_coordinates):
    x = random.uniform(0, 10)
    y = random.uniform(0, height)
    coordinates_x.append(x)
    coordinates_y.append(y)


for _ in range (num_coordinates):
  if coordinates_y[_] <= f(coordinates_x[_]):
    ns = ns + 1
  else:
    continue


x = np.linspace(0, width, 100)

plt.plot(x, f(x), color='red')


plt.scatter(coordinates_x,coordinates_y, s = 1)
print('ns ', ns)

area = height*width*ns/num_coordinates
print('Area: ', area)
plt.show()