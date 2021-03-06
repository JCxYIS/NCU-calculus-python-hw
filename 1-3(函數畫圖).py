import pylab;


# functions
pi = pylab.pi;
def sin(x):
    return pylab.sin(x);
def cos(x):
    return pylab.cos(x);

def f(x):
    # print("a");
    return sin(x) / abs(2*x);


# draw
rangeX, rangeY = -10*pi, 10*pi;
nodeCount = 487;
xpoints = pylab.linspace(rangeX, rangeY, nodeCount);

pylab.plot( xpoints, f(xpoints) );
# pylab.plot( xpoints, g(xpoints) );


# final draw pic
pylab.grid();
pylab.title("This is quite fun though");
pylab.xlabel("Xvideo");
pylab.ylabel("Yvideo")
pylab.show();
