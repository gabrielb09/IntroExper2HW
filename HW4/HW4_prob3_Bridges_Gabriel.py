## problem 2.3
## Gabriel Bridges
## GLB300@nyu.edu

import math

eqA = (2+math.exp(2.8))/(math.sqrt(13)-2)
eqB = (1-(1+math.log(2))**(-3.5))/(1+math.sqrt(5))
eqC = math.sin((2-math.sqrt(2))/(2+math.sqrt(2)))
a = "a"
b = "b"
c = "c"
choice = "a"
while choice != "quit":
	choice = raw_input("Enter 'a','b', or 'c' to see the answer to an equation, enter 'quit' to quit\n")
	if choice == a:
		print(eqA)
	if choice == b:
		print(eqB)
	if choice == c:
		print(eqC)
