import pylab


# functions
pi = pylab.pi;
def sin(x):
    return pylab.sin(x);
def cos(x):
    return pylab.cos(x);

# 定義函示
def f(x):
    return sin(3*x)*cos(3*x)
a = pi/2# 上盒
b = 0  #下和
n = 100 # 分割數

# fn = lambda x: f(x)

# 等分點xs, 算ys
xs, h = pylab.linspace(a, b, n+1, retstep=True)
ys = f(xs)

# 各種和
rsum = 0
lsum = 0
usum = 0
tsum = 0

y1 = ys[0]

# Loop
for y2 in ys[1:] :
    rsum += y1;
    if y1 < y2:
        lsum += y1
        usum += y2
    else:
        lsum += y2
        usum += y1
    tsum += y1+y2
    y1 = y2

# modif
rsum *= h
lsum *= h
usum *= h
tsum *= h/2
isum = -(1/6) # cos^2(3x)/6 

# print
print("數學積分：", round(isum, 9), "\n")
print("迴圈求積：")
print("矩形積分：", round(rsum, 9), "誤差：", round(abs(isum-rsum), 10))
print("上矩形積分：", round(usum, 9), "誤差：", round(abs(isum-usum), 10))
print("下矩形積分：", round(lsum, 9), "誤差：", round(abs(isum-lsum), 10))
print("梯形積分法：", round(tsum, 9), "誤差：", round(abs(isum-tsum), 10))
print("\n")

# 矩形法係數 1 1 1 ... 1 1 1
isum1 = h * sum(ys[:-1])
# 梯形法係數 1 2 2 ... 2 2 1
isum2 = h * sum( [ys[0] , 2*sum(ys[1:-1]), ys[-1] ]) / 2
# Simpson 1/3 rule factor 1 4 2 4 2 ... 2 4 1
isum3 = h * sum([ys[0], 4*sum(ys[1:-1:2]), 2*sum(ys[2:-1:2]), ys[-1]]) / 3

# print
print("公式求積：")
print("矩形積分：", round(isum1, 9), "誤差：", round(abs(isum1-isum), 10))
print("上矩形積分：", round(isum2, 9), "誤差：", round(abs(isum2-isum), 10))
print("下矩形積分：", round(isum3, 9), "誤差：", round(abs(isum3-isum), 10))