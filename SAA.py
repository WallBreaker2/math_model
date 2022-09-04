import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time
# tempature
T = 1.0
T_min = 1e-6
alpha = 0.95
# iteratir count
K_max = 200
# init value of solution
x_k = 2.0
x_best = x_k
# targert function
def f(x):
    return np.power(x,2)

start_tm = time.time()
iter_cnt = 0
# cooling loop
while T > T_min:
    k = 0
    # state loop
    while k < K_max:
        y = x_k + np.random.uniform(-0.2,0.2)
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
print("解:{} 最小值:{:.2f}\n误差:{:.3f}".format(x_best,f(x_best), abs(x_best)))
print("迭代次数:{},用时:{:.2f}s".format(iter_cnt, end_tm - start_tm))
xs = np.linspace(-3,3,100)
ys = f(xs)
plt.plot(xs, ys)


# plt.show()
