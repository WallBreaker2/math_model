import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

from mpl_toolkits import mplot3d
# tempature
T = 1.0
T_min = 1e-6
alpha = 0.96
# iteratir count
K_max = 1000
# init value of solution
x_k = 9
x_best = x_k
# targert function
def f(x):
    return 0.25*np.power(x,4)-2*np.power(x,2)+x +3
def getNewX(x):
    r = 0.5
    # return x + np.array([np.random.uniform(-r,r),np.random.uniform(-r,r)])
    return x + np.random.uniform(-r,r)

def error_f(x):
    return abs(-2.11491-x)
start_tm = time.time()
iter_cnt = 0
# cooling loop
while T > T_min:
    k = 0
    # state loop
    while k < K_max:
        y = getNewX(x_k)
        delta = f(y) - f(x_k)
        if delta <= 0.0:
            x_best = y
        else:
            p = math.exp(-delta / T)
            if random.random() <= p:
                pass
            else:
                # not change
                y = x_k
        x_k = y
        k = k + 1
        iter_cnt = iter_cnt + 1
    # cooling
    T = alpha * T
end_tm = time.time()
print("解:{} 最小值:{:.2f}\n误差:{:.6f}".format(x_best,f(x_best), error_f(x_best)))
print("迭代次数:{},用时:{:.2f}s".format(iter_cnt, end_tm - start_tm))


##
# fig = plt.figure()
# ax = mplot3d.Axes3D(fig)

# X= np.arange(-4, 4, 0.1)
# Y = np.arange(-4,4, 0.1)
# X,Y = np.meshgrid(X, Y)
# R= np.sin(X**2 + Y**2)/(1+ X**2 + Y**2)
# ax.plot_surface(X,Y,R)

x = np.linspace(-5,5,100)
y= f(x)
plt.plot(x, y)
plt.grid(True)
plt.title(r'$f(x)=\frac{1}{4}x^4-2x^2+x+3$')
plt.show()
