## Problem 2.1
## Gabriel Bridges
## GLB300@nyu.eduu
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
t = 0.0
h = [1.2]
v = [5.4]
t = [0]
c = 0
T = 0.5

while c < 500:
	h = h + [h[0] + (v[0]*t[c]) - (0.5*g*(t[c]**2))]
	v = v + [v[0] - g*t[c]]
	t = t + [0.001*c]
	c += 1
print("At time T = 0.5s the ball is " + str(h[c]) + " meters up, and is traveling at " + str(v[c]) + " meters per second")

T = 2.0

while c < 2000:
	h = h + [h[0] + (v[0]*t[c]) - (0.5*g*(t[c]**2))]
	v = v + [v[0] - g*t[c]]
	t = t + [0.001*c]
	c += 1
print("At time T = 2.0s the ball is " + str(h[c]) + " meters up, and is traveling at " + str(v[c]) + " meters per second")
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,h)
plt.xlabel("Time")
plt.ylabel("Height")
plt.subplot(3,1,3)
plt.plot(t,v)
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.show()
