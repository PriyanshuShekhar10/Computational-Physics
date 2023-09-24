# @title Runge-Kutta IV Method
import matplotlib.pyplot as plt


dfn = lambda x, y : -1*x*y

x0 = 1
y0 = 1 
h = 0.1

xval = [x0]
yval = [y0]

x1 = 0

while x1 <= 10:
  x1 = x0 + h
  xval.append(x1)
  f0 = dfn(x0, y0)
  f1 = dfn(x0 + 0.5*h, y0 + 0.5*h*f0)
  f2 = dfn(x0 + 0.5*h, y0 + 0.5*h*f1)
  f3 = dfn(x0 + 0.5*h, y0 + 0.5*h*f2)
  y1 = y0 + (h/6)*(f0 + 2*f1 + 2*f2 + f3)
  yval.append(y1)
  y0 = y1
  x0 = x1




# while x0 <= 10 :
#       x0 = x0 + h
#       xval1.append(x0)
#       f0 = dfn(x0, y0)
#       f1 = dfn(x0 + 0.5*h, y0 + 0.5*f0)
#       f2 = dfn(x0 + 0.5*h, y0 + 0.5*f1)
#       f3 = dfn(x0 + 0.5*h, y0 + 0.5*f2)
#       y1= y0 + h*(f0 + 2*f1 + 2*f2 + f3)/6
#       yval1.append(y1)
#       y0 = y1
      

plt.plot(xval, yval)

plt.show()
