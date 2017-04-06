import numpy as np
import matplotlib.pyplot as plt

n = eval(raw_input("How many dice do you want to roll"))
max = n*6
p =1/float((6**n))
values = np.linspace(n, max, num=(max-(n-1)), dtype=int)
propability = [0] * (max-(n-1))
print propability
c = 0
count = 1
numWays = [0]
while count < n :
	while c < ((max-(n-1))/2):
		numWays[c-1] = numWays[c-2]+c





propability[c] = p*(c+1)
	propability[(len(propability)-1)-c] = p*(c+1)
	c +=1
if (n%2 == 0):
	propability[(len(propability))/2] = p*(c+1)
plt.bar(values, propability)
plt.show()
print sum(propability)
