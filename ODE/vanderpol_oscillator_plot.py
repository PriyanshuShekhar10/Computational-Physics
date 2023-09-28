#Van Der Pol Oscillator
import matplotlib.pyplot as plt
import math

ydot = lambda x,y, e : -1*x - e*(x**2 -1)*y 

y0 = 0
t0 = 0
x0 = 0.5 
e = 1 
tn = 8*math.pi
h=0.01
xval , yval, tval = [x0] , [y0] , [t0]

for i in range(int(tn / h)):
  x1 = x0 + h*y0
  y1 = y0 + h*ydot(x0,y0,e)
  xval.append(x1)
  yval.append(y1)
  t0= t0 + h
  tval.append(t0)

  y0 = y1
  x0 = x1
# print(xval)
# print(tval)
# print(yval)
plt.plot(tval, xval)
plt.plot(tval, yval, 'pink')