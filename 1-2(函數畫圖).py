import pylab;


# functions
pi = pylab.pi;
def sin(x):
    return pylab.sin(x);
def cos(x):
    return pylab.cos(x);

def f(x):
    # print("a");
    return cos(x)**2 / pylab.sqrt( pylab.maximum(1, 2*x-1) );


# draw
rangeX, rangeY = 0, 10*pi;
nodeCount = 487;
xpoints = pylab.linspace(rangeX, rangeY, nodeCount);

pylab.plot( xpoints, f(xpoints) );


# final draw pic
pylab.grid();
pylab.title("I don't like python;");
pylab.xlabel("Xvideo");
pylab.ylabel("Yvideo")
pylab.show();
