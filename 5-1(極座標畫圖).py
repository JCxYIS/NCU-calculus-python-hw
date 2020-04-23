import pylab
from numpy import *


# angmin, angmax, splitPoints
a = 0
b = 14*pi
n = 8763


angs = linspace(a, b, n)

rs = sin(8*angs/7)

pylab.polar( angs, rs, lw=5, label="8theta/7" )

pylab.title("Polar Bear!", color='g')
# pylab.legend()
# pylab.grid()


pylab.show()
