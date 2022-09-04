# 模拟退火算法(Simulated Annealing )
## 简介
模拟退火算法是基于Monte-Carlo 迭代求解策略的一种随机寻优算法


## 流程
给定目标函数$f(x): D \to R$，我们需要求出其在区域$D$上的最小值。假设初值为$x_0$,在$x_0$邻域内取一点$x_1$, 若$f(x_1)\leq f(x_0) $ 则认为$x_1$ 为更优的解，否则，以概率
$e^{-\frac{f(x_1)-f(x_0)}{T}}$ 认为该值为更优解，重复上述操作k次，到达次数后，降低温度T，例如$T=0.95*T$. 当T小于某个设定值时，迭代结束，输出最优解和函数值

![png](./SAA.svg)
## python代码实现
目标函数为 $f(x)=x^2$
```py
import numpy as np
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
```


