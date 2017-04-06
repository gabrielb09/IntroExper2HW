# Intro. Exp. Physics II HW5, Gabriel Bridges
# Problem 3.4
# GLB300@nyu.edu

import numpy as np

height = np.array(np.arange(10,0,-0.5))
t = np.sqrt(((2*(10-height))/9.81))
deltaT = t[1:t.size]-t[0:t.size-1]
Vavg = 0.5/deltaT
print Vavg
