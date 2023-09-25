
import matplotlib.pyplot as plt

m = 1.0       
k = 10.0     
x0 = 1.0     
v0 = 0.0     
h = 0.001       
t_final = 100.0 


t_values= [0.0]
x_values = [x0]
v_values = [v0]


t =0
x=x0
v=v0

while t< t_final:
  a = (-k * x) /m

  x = x + h*v
  v = v + h*a

  t+=h
  t_values.append(t)
  x_values.append(x)
  v_values.append(v)


plt.figure(figsize=(10,6))
plt.plot(t_values, x_values, label='Position(x)')
plt.plot(t_values, v_values, label='Velocity(v)')
plt.xlabel('Time')
plt.ylabel('Position (m) / Velocity(m/s)')
plt.legend()
plt.grid(True)
plt.show()
     
