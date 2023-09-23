from matplotlib import pyplot as plt


x0 = 1
h = 0.01
y0 = 0.01
dfn = lambda x, y : -1*x*y
x1 = 0
y1 = 0
x_val1 = [x0]
y_val1 = [y0]

x_val2 = [x0]
y_val2 = [y0]

while x1 >= -10 :
    x1 = x0 - h
    x_val1.append(x1)
    y1= y0 - h*dfn(x0, y0)
    y_val1.append(y1)
    x0 = x1
    y0 = y1
x0 = 1
h = 0.01
y0 = 0.01
# dfn = lambda x, y : -1*x*y
x1 = 0
y1 = 0
while x1 <= 10 :
    x1 = x0 + h
    x_val2.append(x1)
    y1= y0 + h*dfn(x0, y0)
    y_val2.append(y1)
    x0 = x1
    y0 = y1

plt.plot(x_val1, y_val1, 'b')
plt.plot(x_val2, y_val2,'b')
plt.show()
