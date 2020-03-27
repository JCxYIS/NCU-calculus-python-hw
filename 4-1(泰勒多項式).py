import pylab
import numpy

#
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def taylor_SinPlusCos(n, x):
    totalsum = 0.0
    for k in range(n+1):
        # sinx+cosx: ++--++--輪替
        if k % 4 < 2:
            totalsum += (x**k / factorial(k))
        else:
            totalsum -= (x**k / factorial(k))
        print("K="+str(k)+" | "+str(factorial(k)) + str(k % 4 < 2))
    return totalsum

a = 0
b = 3 * numpy.pi
m = 100

xs = numpy.linspace(a,b,m)

for i in range(1, 19):
    if i % 2 == 0:
        continue
    ys = taylor_SinPlusCos(i, xs)
    pylab.plot( xs, ys, label="P"+str(i) )

pylab.plot( xs, numpy.sin(xs)+numpy.cos(xs), label="SIN+COS" )

pylab.title("I'm sure that Taylor can't program in python")
pylab.legend()
pylab.grid()

pylab.xlabel("Xvideo")
pylab.ylabel("Yvideo")

pylab.ylim(-2, 2)

pylab.show()