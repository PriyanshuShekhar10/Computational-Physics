import matplotlib.pyplot as plt

x_bar = lambda x, y, z: 10*(y - x)
y_bar = lambda  x, y , z: 28*x - y - x*z
z_bar = lambda x, y , z: x*y - (8/3)*z


x0 = 0
y0 = 1
z0 = 0
h = 0.001
xval = [] 
yval = []
zval = []



for _ in range(100000):
  x1 = x0 + h*x_bar(x0, y0, z0)
  xval.append(x1)
  y1 = y0 + h*y_bar(x0, y0, z0)
  yval.append(y1)
  z1 = z0 + h*z_bar(x0, y0, z0)
  zval.append(z1)
  x0 = x1 
  y0 = y1
  z0 = z1


plt.figure().add_subplot(111, projection='3d').plot(xval, yval, zval, lw = 0.5)
plt.show()
