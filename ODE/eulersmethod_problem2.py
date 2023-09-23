from matplotlib import pyplot as plt


x0 = 0
h = 0.01
y0 = 0
dfn = lambda y : y**2 + 1
x1 = 0
y1 = 0
x_val1 = [x0]
y_val1 = [y0]

# x_val2 = [x0]
# y_val2 = [y0]

while x1 <= 1 :
    x1 = x0 + h
    x_val1.append(x1)
    y1= y0 + h*dfn(y0)
    y_val1.append(y1)
    x0 = x1
    y0 = y1

plt.plot(x_val1, y_val1)
plt.show()