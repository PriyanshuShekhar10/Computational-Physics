import matplotlib.pyplot as plt

def f(x,y,z):
  x_bar = 10*(y - x)
  y_bar = 28*x - y - x*z
  z_bar = x*y - (8/3)*z
  return x_bar, y_bar, z_bar

x0, y0, z0, dt = 0,1,0,0.00001
xval, yval, zval = [x0], [y0], [z0] 

for _ in range (int(100/dt)):
    x_dot, y_dot, z_dot = f(x0, y0, z0)

    x1 = x0 + dt * x_dot
    y1 = y0 + dt * y_dot
    z1 = z0 + dt * z_dot

    xval.append(x1)
    yval.append(y1)
    zval.append(z1)
    x0 , y0 , z0 = x1 , y1, z1



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xval, yval, zval, lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Plot')


a2d = plt.figure().add_subplot()
a2d.plot(xval, yval, lw=0.3)
a2d.set_xlabel('X')
a2d.set_ylabel('Y')
a2d.set_title('2D Plot (X-Y Plane)')
a2d.grid()



plt.show()
