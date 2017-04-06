## problem 2.2
## Gabriel Bridges
## GLB300@nyu.edu

import math

vo = 10.0
a = 2.5
z = 4.0 + (1/3)
V=vo*(1-(z/math.sqrt(((a**2)+(z**2)))))
print (V)
z = 8.0 + (2/3)
V=vo*(1-(z/math.sqrt(((a**2)+(z**2)))))
print(V)
z = 13.0
V=vo*(1-(z/math.sqrt(((a**2)+(z**2)))))
print(V)
