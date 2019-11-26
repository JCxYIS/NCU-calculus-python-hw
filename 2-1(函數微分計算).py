import pylab;


# functions
pi = pylab.pi;
def sin(x):
    return pylab.sin(x);
def cos(x):
    return pylab.cos(x);

def f(x):
    # print("a");
    return ( 2+sin(x/pi) ) / ( 2-sin(x/pi) );

def DerivativeF(x):
    # error value
    h = 0.00000000001;
    return ( f(x+h) - f(x) ) / h;


# draw
rangeX, rangeY = 0, 51;
nodeCount = 487;
xpoints = pylab.linspace(rangeX, rangeY, nodeCount);

pylab.plot( xpoints, f(xpoints) );
pylab.plot( xpoints, DerivativeF(xpoints) );
# pylab.plot( xpoints, g(xpoints) );


# final draw pic
pylab.grid();
pylab.title("AAAAAAAAAAAAAAAAAAAAAAAAAAAA");
pylab.xlabel("Xvideo");
pylab.ylabel("Yvideo")
pylab.show();
