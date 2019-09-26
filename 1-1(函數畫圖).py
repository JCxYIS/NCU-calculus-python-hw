import pylab;


# functions
pi = pylab.pi;
def sin(x):
    return pylab.sin(x);
def cos(x):
    return pylab.cos(x);

def f(x):
    # print("a");
    return pylab.maximum( abs(x*sin(x)), abs(x*cos(x)) );
def g(x):
    # print("a");
    return pylab.minimum( abs(x*sin(x)), abs(x*cos(x)) );


# draw
rangeX, rangeY = -2*pi, 2*pi;
nodeCount = 487;
xpoints = pylab.linspace(rangeX, rangeY, nodeCount);

pylab.plot( xpoints, f(xpoints) );
pylab.plot( xpoints, g(xpoints) );


# final draw pic
pylab.grid();
pylab.title("Please read 228922.");
pylab.xlabel("Xvideo");
pylab.ylabel("Yvideo")
pylab.show();
