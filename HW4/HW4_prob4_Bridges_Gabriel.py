## problem 2.4
## Gabriel Bridges
## GLB300@nyu.edu
import cmath
a = float(raw_input("what is a?\n"))
b = float(raw_input("what is b?\n"))
c = float(raw_input("what is c?\n"))
a = a+0j
b = b+0j
c = c+0j
xa = (((-1*b)+cmath.sqrt((b**2)-(4*a*c)))/(2*a))
xb = (((-1*b)-cmath.sqrt((b**2)-(4*a*c)))/(2*a))

print("The roots are: {0:0.3f} + {1:0.3f}i and {2:0.3f} + {3:0.3f}i".format(xa.real,xa.imag,xb.real,xb.imag))
